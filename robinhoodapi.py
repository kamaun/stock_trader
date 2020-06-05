import robin_stocks as bot_trader
import sys, os
from decouple import config, Csv


try:
    sign_in = bot_trader.login(username=config('USERNAME'), password=config('PASSWORD'))
except Exception as login_err:
    print(str(login_err))


def exception_log(err):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name, exception = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1], exc_type.__name__
    line, message = str(exc_tb.tb_lineno), str(err)
    print(f'{exception}\tFile: {file_name} | Line: {line} Message: {message}')


def view_holdings():
    print("\nPresenting all current user holdings")
    print('---------------------------- --------')
    try:
        for ticker, data in bot_trader.build_holdings().items():
            print(ticker, ': ')
            for key, value in data.items():
                print('\t', key, ': ', value)
    except Exception as holdings_err:
        exception_log(holdings_err)
    print('------------------------------------\n')


def buy_shares(symbol, amount):
    print(f'\nBuying {amount} share(s) from {symbol}')
    print('------------------------------------')
    try:
        bot_trader.order_buy_market(symbol=symbol, quantity=amount)
    except Exception as holdings_err:
        exception_log(holdings_err)
    print('------------------------------------\n')


def sell_shares(symbol, amount):
    print(f'\nSelling {amount} share(s) from {symbol}')
    print('------------------------------------')
    try:
        bot_trader.order_sell_market(symbol=symbol, quantity=amount)
    except Exception as holdings_err:
        exception_log(holdings_err)
    print('------------------------------------\n')


def buy_crypto(symbol, amount):
    print(f'\nBuying {symbol} crypto coins')
    print('------------------------------------')
    try:
        bot_trader.order_buy_crypto_by_price(symbol=symbol, amountInDollars=amount)
    except Exception as holdings_err:
        exception_log(holdings_err)
    print('------------------------------------\n')
