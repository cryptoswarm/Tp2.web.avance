import pytz
# from inf5190_projet_src import create_app
from inf5190_projet_src import application
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from config import JOB_STORE_URL, JOB_STORES, JOB_DEFAULTS
from inf5190_projet_src.models.scheduler_test import SchedulerTest
from inf5190_projet_src.repositories.test_insert_scheduler import add

def test():
    with application.app_context():
        print('Display to console not in logging : Task is running {} :'.format(datetime.now()))
        logging.info('Task is running')

# def db_insertion():
#     with application.app_context():
#         instance = SchedulerTest('name', datetime.now())
#         created_instance = add(instance)
#         logging.info('created instance :',created_instance)

def setting_job_1():
    with application.app_context():
        persist_patinoir_data()

def setting_job_2():
    with application.app_context():
        persist_aqua_data() 

def setting_job_3():
    with application.app_context():
        persist_glissade_data()


def run_jobs():
    with application.app_context():
        scheduler = BackgroundScheduler(jobstores=JOB_STORES, job_defaults=JOB_DEFAULTS)
        scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.add_job(func=setting_job_3, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        #scheduler.add_job(func=test, trigger='interval', seconds=59, timezone=pytz.timezone('CANADA/EASTERN'))
        #scheduler.add_job(func=db_insertion, trigger='interval', seconds=59, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.start()


if __name__ == "__main__":
    # run_jobs()
    application.run(debug=True)
    