import sqlite3
import os, sys
from datetime import datetime

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


def get_sys_info(err_msg):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    exception = exc_type.__name__
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    line = str(exc_tb.tb_lineno)
    message = str(err_msg)
    msg = "%s\tFile: %s; line: %s - %s\n" % (exception, fname, line, message)
    print(msg)
    log_error(exception=exception, file=fname, line=line, message=message)


def setup():
    try:
        cursor.execute('CREATE TABLE error_logs (date, exception, file, line, message)')
        cursor.execute('CREATE TABLE activity_log (date, action)')
        cursor.execute(
            'CREATE TABLE trading_logs (date, ticker_symbol, activity, list_price, quantity, total, profit_loss)'
        )
        log_activity("run set up ")
    except Exception as setup_err:
        get_sys_info(setup_err)


def log_activity(action=None):
    cursor.execute('INSERT INTO activity_log VALUES ("%s", "%s")' % (datetime.now(), action))


def log_error(**kwargs):
    cursor.execute(
        'INSERT INTO error_logs VALUES ("%s", "%s", "%s", "%s", "%s")' % (datetime.now(), kwargs['exception'], kwargs['file'], kwargs['line'], kwargs['message'])
    )


log_activity("run set up ")
