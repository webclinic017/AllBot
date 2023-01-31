# import logging
# from binance.spot import Spot as Client
# from binance.lib.utils import config_logging
# from binance.error import ClientError
#
# config_logging(logging, logging.DEBUG)
#
# key = "VI6hVdW4xVtr4CXponITFo4217t2Xoxx0xcSfbZUfUupOV1on2GgPPBBYUbLamrn"
# secret = "l2oqsYuxpGfQzSmS9WeEvKRGdjsFEQEgzNCkGIg7x49o8nEOZjOgppcamgGN5qLv"
#
# client = Client(key, secret, base_url="https://testnet.binance.vision")
# logging.info(client.account(recvWindow=6000))
#
# params = {
#         "symbol": "BTCUSDT",
#         "side": "BUY",
#         "type": "MARKET",
#         "quoteOrderQty": 20
# }
#
# try:
#     response = client.new_order(**params)
#     logging.info(response)
# except ClientError as error:
#     logging.error(
#         "Found error. status: {}, error code: {}, error message: {}".format(
#             error.status_code, error.error_code, error.error_message
#         )
#     )