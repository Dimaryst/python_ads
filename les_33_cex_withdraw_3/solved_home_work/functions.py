import ccxt

from config import okx_api_key, okx_api_secret, okx_api_secret_phrase, binance_api_key, binance_api_secret


def okx_withdraw_eth_arbitrum(address: str, amount: float) -> None:
    """
    Withdraw ETH from OKX to Arbitrum one
    :param address: address of the wallet
    :param amount: amount of withdrawal
    :return: None
    """

    exchange = ccxt.okx({
        'apiKey': okx_api_key,
        'secret': okx_api_secret,
        'password': okx_api_secret_phrase,
    })
    code = "ETH"
    network = "Arbitrum one"
    params = {
        "ccy": code,
        "toAddr": address,
        "amt": amount,
        "fee": "0.0001",
        "dest": "4",
        "chain": f"{code}-{network}"
    }
    tx = exchange.withdraw(code, amount, address, params=params)
    print(tx)


def okx_withdraw_eth_optimism(address: str, amount: float) -> None:
    """
       Withdraw ETH from OKX to optimism
       :param address: address of the wallet
       :param amount: amount of withdrawal
       :return: None
   """

    exchange = ccxt.okx({
        'apiKey': okx_api_key,
        'secret': okx_api_secret,
        'password': okx_api_secret_phrase,
    })
    code = "ETH"
    network = "Optimism"
    params = {
        "ccy": code,
        "toAddr": address,
        "amt": amount,
        "fee": "0.00004",
        "dest": "4",
        "chain": f"{code}-{network}"
    }
    tx = exchange.withdraw(code, amount, address, params=params)
    print(tx)


def binance_withdraw_eth_arbitrum(address: str, amount: float) -> None:
    """
    Withdraw ETH from Binance to Arbitrum one
    :param address: address of the wallet
    :param amount: amount of withdrawal
    :return: None
    """
    exchange = ccxt.binance({
        'apiKey': binance_api_key,
        'secret': binance_api_secret
    })
    tx = exchange.withdraw("ETH", amount, address, params={"network": "ARBITRUM"})
    print(tx)


def get_balance(exchange: ccxt.Exchange) -> dict:
    """
    Get the balance of the account
    :param exchange: подключение к бирже к конкретному аккаунту
    :return: словарь с балансами
    """
    balances = {}
    if exchange.name == "OKX":
        balances["spot"] = exchange.fetch_balance({"type": "spot"})
        balances["funding"] = exchange.fetch_balance({"type": "funding"})
    elif exchange.name == "Binance":
        balances["spot"] = exchange.fetch_balance({"type": "spot"})
        balances["funding"] = exchange.fetch_balance({"type": "funding"})
        balances["margin"] = exchange.fetch_balance({"type": "margin"})
    elif exchange.name == "Bybit":
        balances["spot"] = exchange.fetch_balance({"type": "spot"})
        balances["FUND"] = exchange.fetch_balance({"type": "FUND"})
    else:
        print("Unknown exchange")
        return {}
    return balances


def get_balance_okx(exchange: ccxt.okx) -> dict:
    """
    Get the balance of the account
    :param exchange: подключение к бирже к конкретному аккаунту
    :return:  словарь с балансами
    """
    print(exchange.name == "OKX")
    print(ccxt.binance().fetch_balance())
    print(ccxt.bybit().fetch_balance())
    balance = exchange.fetch_balance({"type": "funding"})
    return balance


def get_okx_tokens() -> list:
    my_list = list()
    markets = ccxt.okx().fetch_markets()
    for value in markets:
        my_list.append(value["symbol"])

    return my_list


def get_binance_tokens() -> list:
    my_list = list()
    markets = ccxt.binance().fetch_markets()
    for value in markets:
        my_list.append(value["symbol"])

    return my_list


if __name__ == '__main__':
    pass
    # private_api()
    # my_list = get_okx_tokens()
    # for token in my_list:
    #     print(token)
    # my_list = get_binance_tokens()
    # for token in my_list:
    #     print(token)
