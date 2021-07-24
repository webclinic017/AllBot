from binance.spot import Spot as Client
from binance.error import ClientError
from app.database.Schemas import *
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
        # position = PositionSchema()
        # position.entryOrderId = response['orderId']
        # position.entryPrice = response['orderId']
        # position.entryQuantity = response['executedQty']
        # PositionSchema().save()
        return response['orderId']

    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


def sellMarket(robot, price):
    params = {
        "symbol": robot.symbol,
        "side": "SELL",
        "type": "MARKET",
        "timeInForce": "GTC",
        "quantity": robot.quantity,
        "price": price,
    }
    client = Client(robot.key, robot.secret, base_url=BASE_URL)
    try:
        response = client.new_order(**params)
        logging.info(response)
        return response['orderId']
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


def cancelOpenOrders(robot):
    client = Client(robot.key, robot.secret, base_url=BASE_URL)
    try:
        response = client.cancel_open_orders(robot.symbol)
        logging.info(response)
        return True
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


def closePosition(robot):
    if robot.side == "BUY":
        side = "SELL"
    else:
        side = "BUY"
    params = {
        "symbol": robot.symbol,
        "side": side,
        "type": "MARKET",
        "quoteOrderQty": robot.quantity,
    }
    client = Client(robot.key, robot.secret, base_url=BASE_URL)
    try:
        response = client.new_order(**params)
        logging.info(response)
        return True

    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
