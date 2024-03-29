from src.database.Schemas import RobotSchema, PositionSchema
from src.mobileNotify.SendNotify import sendTelegramMessage
from binance.spot import Spot as Client
from binance.error import ClientError
from bson import ObjectId
import logging

BASE_URL = "https://testnet.binance.vision"


def buyMarket(robot):
    params = {
        "symbol": robot.symbol,
        "side": "BUY",
        "type": "MARKET",
        "quoteOrderQty": robot.quantity,
    }
    client = Client(robot.key, robot.secret, base_url=BASE_URL)

    try:
        response = client.new_order(**params)
        logging.info(response)
        updateEntryPosition(robot, "BUY", response)
        message = 'O seu Robô: ' + robot.nickName + ' realizou uma compra de U$' + str(response['cummulativeQuoteQty']) + ' em ' + robot.comb[:3]
        sendTelegramMessage(message, robot.chatID)
        return response['orderId']

    except ClientError as error:
        logging.error("Found error. status: {}, error code: {}, error message: {}".format(error.status_code, error.error_code, error.error_message))


def sellMarket(robot):
    params = {
        "symbol": robot.symbol,
        "side": "SELL",
        "type": "MARKET",
        "quoteOrderQty": robot.quantity,
    }
    client = Client(robot.key, robot.secret, base_url=BASE_URL)

    try:
        response = client.new_order(**params)
        logging.info(response)
        updateEntryPosition(robot, "SELL", response)
        message = 'O seu Robô: ' + robot.nickName + ' realizou uma venda de U$' + str(response['cummulativeQuoteQty']) + ' em ' + robot.comb[:3]
        sendTelegramMessage(message, robot.chatID)
        return response['orderId']

    except ClientError as error:
        logging.error("Found error. status: {}, error code: {}, error message: {}".format(error.status_code, error.error_code, error.error_message))


def closePosition(robot):
    robotSchema = RobotSchema.objects(id=ObjectId(robot.id)).first()
    position = robotSchema.positions and robotSchema.positions[-1]
    if position and position.open:
        if position.side == "BUY":
            side = "SELL"
        else:
            side = "BUY"
        params = {
            "symbol": robot.symbol,
            "side": side,
            "type": "MARKET",
            "quantity": position.entryQuantity,
        }
        client = Client(robot.key, robot.secret, base_url=BASE_URL)
        try:
            response = client.new_order(**params)
            logging.info(response)
            position.closeOrderId = response['orderId']
            position.closeQuantity = float(response['executedQty'])
            position.closeCummulativeQuoteQty = float(response['cummulativeQuoteQty'])
            position.open = False
            position.profit = position.closeCummulativeQuoteQty - position.entryCummulativeQuoteQty
            position.profitPercentage = ((position.closeCummulativeQuoteQty / position.entryCummulativeQuoteQty) - 1) * 100
            robotSchema.positions[-1] = position
            robotSchema.save()
            message = 'O seu Robô: ' + robot.nickName + ' encerrou a operação em ' + robot.comb[:3] + ' com U$ ' + position.profit
            sendTelegramMessage(message, robot.chatID)
            return True

        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )


def updateEntryPosition(robot, side, response):
    robotSchema = RobotSchema.objects(id=ObjectId(robot.id)).first()
    position = PositionSchema()
    position.side = side
    position.entryOrderId = response['orderId']
    position.entryQuantity = float(response['executedQty'])
    position.entryCummulativeQuoteQty = float(response['cummulativeQuoteQty'])
    position.open = True
    robotSchema.positions.append(position)
    robotSchema.save()


