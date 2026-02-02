import os
import subprocess
import schedule
import time

# def remind_commit():
#     os.system('notify-send "Reminder: Push your code before dinner!"')

# schedule.every().day.at("19:00").do(remind_commit)

while True:
    # print('runs')
    subprocess.Popen('echo Hello World!', shell=True)
    os.system('pwd')
    # schedule.run_pending()
    time.sleep(5)