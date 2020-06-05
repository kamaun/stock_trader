import os
import sqlite3
import sys
from datetime import datetime

conn = sqlite3.connect('trader.db')
cursor = conn.cursor()


def get_sys_info(err_msg):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    exception, file_name = exc_type.__name__, os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    line, message = str(exc_tb.tb_lineno), str(err_msg)
    msg = "%s\tFile: %s; line: %s - %s\n" % (exception, file_name, line, message)
    log_error(exception=exception, file=file_name, line=line, message=message)
    print(msg)


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


def log_activity(action='Testing'):
    try:
        cursor.execute('INSERT INTO activity_log VALUES (?,?)', (datetime.now(), action,))
    except Exception as setup_err:
        get_sys_info(setup_err)


def log_error(**kwargs):
    try:
        cursor.execute(
            'INSERT INTO error_logs VALUES (?,?,?,?,?)',
            (datetime.now(), kwargs['exception'], kwargs['file'], kwargs['line'], kwargs['message'],)
        )
    except Exception as setup_err:
        get_sys_info(setup_err)


# setup()
# log_activity()
# log_activity()
# log_activity()

cursor.execute('SELECT * FROM activity_log ORDER BY date')
for row in cursor.fetchall():
    print(row)

cursor.close()
