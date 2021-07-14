import urllib
import requests
import time
import hashlib
import hmac

apikey = "ILBDb6uATI7e50vDp7NtPiKhnonJ1ubDxJW7DScLkih2eaBoW0Wc3sIVpArbx40K"
secret = "ICeBRRrLX5rHNIIOHPyOX2coxqEVk1yPgTN44briSVjhrk1xutTtDTqtyERLzMCu"


def orders(var1):
    global apikey, secret, hashedsig
    servertimeint = getServerTime()

    params = urllib.parse.urlencode({
        "symbol": var1,
        "timestamp": servertimeint,
    })
    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.get("https://api.binance.com/api/v3/allOrders",
                            params={
                                "symbol": var1,
                                "timestamp": servertimeint,
                                "signature": hashedsig,
                            },
                            headers={
                                "X-MBX-APIKEY": apikey,
                            }
                            )

    return userdata.json()


def getBalance():
    global apikey, secret, hashedsig
    servertimeint = getServerTime()

    params = urllib.parse.urlencode({
        "timestamp": servertimeint,
    })

    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.get("https://api.binance.com/api/v3/account",
                            params={
                                "timestamp": servertimeint,
                                "signature": hashedsig,
                            },
                            headers={
                                "X-MBX-APIKEY": apikey,
                            }
                            )

    return userdata.json()


def cancelOrder(symbol, orderID):
    global apikey, secret
    servertimeint = getServerTime()

    params = urllib.parse.urlencode({
        "symbol": symbol,
        "orderId": orderID,
        "timestamp": servertimeint,
    })

    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.delete("https://api.binance.com/api/v3/order",
                               params={
                                   "symbol": symbol,
                                   "orderId": orderID,
                                   "timestamp": servertimeint,
                                   "signature": hashedsig,
                               },
                               headers={
                                   "X-MBX-APIKEY": apikey,
                               }
                               )
    print(userdata.text)
    return userdata.json()


def limit(symbol, side, quantity, price):
    global apikey, secret
    servertimeint = getServerTime()

    params = urllib.parse.urlencode({
        "symbol": symbol,
        "side": side,
        "type": "limit",
        "quantity": quantity,
        "price": price,  #USDT
        "timeInForce": "GTC",
        "timestamp": servertimeint,
    })

    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.post("https://api.binance.com/api/v3/order",
                             params={
                                 "symbol": symbol,
                                 "side": side,
                                 "type": "limit",
                                 "quantity": quantity,
                                 "price": price,
                                 "timeInForce": "GTC",
                                 "timestamp": servertimeint,
                                 "signature": hashedsig,
                             },
                             headers={
                                 "X-MBX-APIKEY": apikey,
                             }
                             )
    print(userdata.text)
    return userdata.json()


def market(symbol, side, quantity):
    global apikey, secret
    servertimeint = getServerTime()

    if side == "buy":
        prm1 = "quoteOrderQty"  # quoteOrderQty em USDT
    else:
        prm1 = "quantity"  # quantity na moeda

    params = urllib.parse.urlencode({
        "symbol": symbol,
        "side": side,
        "type": "market",
        prm1: quantity,
        "timestamp": servertimeint,
    })

    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.post("https://api.binance.com/api/v3/order",
                             params={
                                 "symbol": symbol,
                                 "side": side,
                                 "type": "market",
                                 prm1: quantity,
                                 "price": None,
                                 "timestamp": servertimeint,
                                 "signature": hashedsig,
                             },
                             headers={
                                 "X-MBX-APIKEY": apikey,
                             }
                             )
    print(userdata.text)
    return userdata.json()


def oco(symbol, side, quantity, price, stopPrice, stopLimitPrice):
    global apikey, secret
    servertimeint = getServerTime()

    params = urllib.parse.urlencode({
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stopPrice": stopPrice,
        "stopLimitPrice": stopLimitPrice,
        "stopLimitTimeInForce": "GTC",
        "timestamp": servertimeint,
    })

    hashedsig = hmac.new(secret.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    userdata = requests.post("https://api.binance.com/api/v3/order/oco",
                             params={
                                 "symbol": symbol,
                                 "side": side,
                                 "quantity": quantity,
                                 "price": price,
                                 "stopPrice": stopPrice,
                                 "stopLimitPrice": stopLimitPrice,
                                 "stopLimitTimeInForce": "GTC",
                                 "timestamp": servertimeint,
                                 "signature": hashedsig,
                             },
                             headers={
                                 "X-MBX-APIKEY": apikey,
                             }
                             )
    print(userdata.text)
    return userdata.json()


def getServerTime():
    # servertime = requests.get("https://api.binance.com/api/v1/time")
    # servertimeobject = json.loads(servertime.text)
    # servertimeint = servertimeobject['serverTime']
    return int(time.time()) * 1000

#print(getBalance())
