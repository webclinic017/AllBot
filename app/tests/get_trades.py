# import logging
# from binance.spot import Spot as Client
# from binance.lib.utils import config_logging
#
# config_logging(logging, logging.DEBUG)
#
# key = "VI6hVdW4xVtr4CXponITFo4217t2Xoxx0xcSfbZUfUupOV1on2GgPPBBYUbLamrn"
# secret = "l2oqsYuxpGfQzSmS9WeEvKRGdjsFEQEgzNCkGIg7x49o8nEOZjOgppcamgGN5qLv"
#
# client = Client(key, secret, base_url="https://testnet.binance.vision")
# logging.info(client.my_trades("BTCUSDT"))
#
# # set the limit
# logging.info(client.my_trades("BTCUSDT", limit=2))
#
# # set the fromId
# logging.info(client.my_trades("BTCUSDT", fromId="10"))
#
# # set startTime and endTime
# logging.info(
#     client.my_trades(
#         "BTCUSDT", limit=2, startTime="1585282456000", endTime="1585368856000"
#     ))
#
