import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *
from config import JOB_STORES, JOB_DEFAULTS
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

appplication = create_app()

def setting_job_1():
    with appplication.app_context():
        persist_patinoir_data()

def setting_job_2():
    with appplication.app_context():
        persist_aqua_data() 

def setting_job_3():
    with appplication.app_context():
        persist_glissade_data()


def run_jobs():
    with appplication.app_context():
        scheduler = BackgroundScheduler(jobstores=JOB_STORES, job_defaults=JOB_DEFAULTS)
        scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.utc)
        scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.utc)
        scheduler.add_job(func=setting_job_3, trigger='interval', hours=24, timezone=pytz.utc)
        scheduler.start()


if __name__ == "__main__":
    run_jobs()
    appplication.run(debug=True)
    