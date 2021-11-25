import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


# One of dev, prod or test
application = create_app('dev')

def test():
    with application.app_context():
        print('Display to console not in logging : Task is running {} :'.format(datetime.now()))
        logging.info('Task is running every 15 min')

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
        scheduler = BackgroundScheduler(jobstores=application.config['JOB_STORES'], job_defaults=application.config['JOB_DEFAULTS'])
        scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.add_job(func=setting_job_3, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.add_job(func=test, trigger='interval', minutes=15, timezone=pytz.timezone('CANADA/EASTERN'))
        scheduler.start()


if __name__ == "__main__":
    run_jobs()
    application.run()
    