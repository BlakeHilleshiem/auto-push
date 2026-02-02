import os
import subprocess
import schedule
import time
from datetime import datetime
import csv
from config import commit_days
print(commit_days)
days_order=['monday','tuesday','wednesday','thrusday','friday','saturday', 'sunday']
day_indexes = [days_order.index(day) for day in commit_days]
print(day_indexes)


# def remind_commit():
#     os.system('notify-send "Reminder: Push your code before dinner!"')

# schedule.every().day.at("19:00").do(remind_commit)
    # subprocess.Popen('echo Hello World!', shell=True)
    # os.system('pwd')
    # schedule.run_pending()
now= datetime.now()
day_idx = now.weekday()

print(day_idx)
while True:
    now_time_utc = datetime.now()
    data={'message':'default msg', 'utc_date':now_time_utc}
    with open('./history.csv', 'w', newline="") as csvfile:
        fieldnames=['message', 'utc_date']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerow(data)
    
    os.system('git add ./history.csv')
    os.system(f'git commit -m "adds commit for {now_time_utc}"')
    os.system('git push')
    sleep_time = 60 * 60 * 24
    time.sleep(sleep_time)