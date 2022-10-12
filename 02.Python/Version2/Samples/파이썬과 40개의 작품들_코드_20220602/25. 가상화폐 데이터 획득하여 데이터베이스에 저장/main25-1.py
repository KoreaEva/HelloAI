import pyupbit

coin_lists = pyupbit.get_tickers(fiat='KRW')
print(coin_lists)

price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)