from datetime import datetime, date
import os


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1 + " " + current_time


def set_current_time(date_now, time):
    os.system(f'date -s {date_now}')
    os.system(f'date +%T -s {time}')


if __name__ == "__main__":
    get_current_time()
    set_current_time("261221", "160853")
