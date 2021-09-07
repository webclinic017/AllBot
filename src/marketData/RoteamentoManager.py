from src.database.Schemas import RobotSchema, PositionSchema
from src.mobileNotify.SendNotify import sendTelegramMessage
from binance.spot import Spot as Client
from binance.error import ClientError
from bson import ObjectId
import logging

BASE_URL = "https://testnet.binance.vision"


def buyMarket(robot):
    if robot.onlyNotify:
        message = 'robot: ' + robot.nickName + '\n' + 'symbol: ' + robot.symbol + '\n' + 'side: BUY'
        sendTelegramMessage(message, robot.chatID)
    else:
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
            message = 'robot: ' + robot.nickName + '\n' +'symbol: ' + robot.symbol + '\n' + 'side: BUY' + '\n' + 'quoteOrderQty: ' + str(response['executedQty'])
            sendTelegramMessage(message, robot.chatID)
            return response['orderId']

        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )


def sellMarket(robot):
    if robot.onlyNotify:
        sendTelegramMessage('robot: ' + robot.nickName + '\n' +
                'symbol: ' + robot.symbol + '\n' +
                'side: SELL')
    else:
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
            sendTelegramMessage('robot: ' + robot.nickName + '\n' +
                    'symbol: ' + robot.symbol + '\n' +
                    'side: SELL' + '\n' +
                    'quoteOrderQty: ' + str(response['executedQty']))
            return response['orderId']

        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )


def closePosition(robot):
    if robot.onlyNotify:
        sendTelegramMessage('robot: ' + robot.nickName + '\n' +
                'symbol: ' + robot.symbol + '\n' +
                'Close Position')
    else:
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
                robotSchema.save()

                sendTelegramMessage('robot: ' + robot.nickName + '\n' +
                        'symbol: ' + robot.symbol + '\n' +
                        'side: ' + side + '\n' +
                        'closeCummulativeQuoteQty: ' + str(position.closeCummulativeQuoteQty))
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

