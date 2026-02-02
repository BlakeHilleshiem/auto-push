import os
import time
from datetime import datetime
import csv

from config import commit_days

days_order=['monday','tuesday','wednesday','thrusday','friday','saturday', 'sunday']
commit_day_indexes = [days_order.index(day) for day in commit_days]

now= datetime.now()

while True:
    now_time_utc = datetime.now()
    day_idx = now_time_utc.weekday()

    if day_idx in commit_day_indexes:
        data={'message':'default msg', 'utc_date':now_time_utc}
        with open('./history.csv', 'a', newline="") as csvfile:
            fieldnames=['message', 'utc_date']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerow(data)
        
        os.system('git add ./history.csv')
        os.system(f'git commit -m "adds commit for {now_time_utc}"')
        os.system('git push')

    sleep_time = 60 * 60 * 24
    time.sleep(sleep_time)