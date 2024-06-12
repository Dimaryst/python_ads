from pprint import pprint

import ccxt

from config import *
from functions import get_okx_fee



def main():

    # exchange = ccxt.okx({
    #     'apiKey': okx_api_key,
    #     'secret': okx_api_secret,
    #     'password': okx_api_secret_phrase,
    # })
    # exchange.load_markets()
    # pprint(exchange.currencies)




    #
    # if is_proxy:
    #     exchange.proxies = proxies
    #
    #
    # proxy = "http://login:password@ip:port"
    # code = "ETH"
    # network = "Arbitrum one"
    # amount = 0.001
    # address = "0xAC8ce8fbC80115a22a9a69e42F50713AAe9ef2F7"
    # params = {
    #     "ccy": code,
    #     "toAddr": address,
    #     "amt": amount,
    #     "fee": "0.0001",
    #     "dest": "4",
    #     "chain": f"{code}-{network}"
    # }
    # tx = exchange.withdraw(code, amount, address, params=params)
    # print(tx)
    # exchange.fetch_currencies()
    #
    # exchange = ccxt.binance({
    #     'apiKey': binance_api_key,
    #     'secret': binance_api_secret
    # })
    # exchange.load_markets()
    # pprint(exchange.currencies)

    exchange = ccxt.bybit({
        'apiKey': bybit_api_key,
        'secret': bybit_api_secret,
    })
    exchange.load_markets()
    pprint(exchange.currencies)
    # for exchange in [okx, binance, bybit]:
    #     print(exchange.name)
    #     pprint(exchange.fetch_balance())
    #     print()


if __name__ == '__main__':
    main()
