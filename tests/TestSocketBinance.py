import json

import websocket

SOCKET = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1m"

def on_open(ws):
    print('opened connection')


def on_close(ws):
    print('closed connection')


def on_message(ws, message):
    #message = json.load(message)
    print(message)


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()

