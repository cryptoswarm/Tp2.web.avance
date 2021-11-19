import pytz
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from inf5190_projet_src.mod_app.controllers import time
from config import UPLOAD_FOLDER
import logging

# app = Flask(__name__)
sched = BackgroundScheduler()

# app.route("/")
# def index():
#     return "welcom to the scheduler!"

def scheduled_task():
    with open(UPLOAD_FOLDER+'/schedul.txt', 'a') as file:
        file.write("this task is running wvery 5 second\n")

def scheduled_task_1():
    with open(UPLOAD_FOLDER+'/schedul.txt', 'a') as file:
        file.write("****this task is running wvery 15 second****\n")


def scheduled_task_2():
    with open(UPLOAD_FOLDER+'/schedul.txt', 'a') as file:
        file.write("****this task is running wvery 15 second****\n")
        time_now = time()
        file.write(time_now)

def scheduled_task_3():
    with open(UPLOAD_FOLDER+'/schedul.txt', 'a') as file:
        file.write("****this task is running wvery 15 second****\n")

def scheduled_task_4():
    logging.info("****this task is running wvery 15 second****\n")

        

# if __name__ == '__main__':
#     print('hello world!')
#     sched.add_job(id='Scheduled task', func=scheduled_task, trigger='interval', seconds=5, timezone=pytz.timezone('CANADA/EASTERN'))
#     sched.add_job(id='Scheduled task_1', func=scheduled_task_1, trigger='interval', seconds=15, timezone=pytz.timezone('CANADA/EASTERN'))
#     sched.start()
#     sched.shutdown()
#     app.run(host='0.0.0.0', port=8000)


print('hello world!')
# sched.add_job(id='Scheduled task', func=scheduled_task, trigger='interval', seconds=5, timezone=pytz.timezone('CANADA/EASTERN'))
# sched.add_job(id='Scheduled task_1', func=scheduled_task_1, trigger='interval', seconds=15, timezone=pytz.timezone('CANADA/EASTERN'))
#sched.add_job(id='Time_1', func=scheduled_task_2, trigger='interval', seconds=15, timezone=pytz.timezone('CANADA/EASTERN'))
sched.add_job(id='Time_3', func=scheduled_task_4, trigger='interval', seconds=15, timezone=pytz.timezone('CANADA/EASTERN'))
sched.start()
#sched.shutdown()
