import robin_stocks as dat_trader
from decouple import config, Csv


try:
    sign_in = dat_trader.login(username=config('USERNAME'), password=config('PASSWORD'))
except Exception as login_err:
    print(str(login_err))




