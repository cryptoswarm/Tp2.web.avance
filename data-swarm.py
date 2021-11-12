import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import start_glissade_scheduler
from config import JOB_STORES
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

appplication = create_app()
# def run_job(app):
#     with app.app_context():
#         #Import function that will be executed by the scheduler
#         # from inf5190_projet_src.controllers.data_requester import save_uploaded_data
#         scheduler = BackgroundScheduler(jobstores=JOB_STORES)
#         #scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
#         scheduler.add_job(func=save_uploaded_data, trigger='interval', minutes=2, timezone=pytz.utc)  #timezone=pytz.utc.dst
#         #start the scheduler
#         scheduler.start()

def setting_job():
    with appplication.app_context():
        start_glissade_scheduler()

def run_job():
    with appplication.app_context():
        scheduler = BackgroundScheduler(jobstores=JOB_STORES)
        scheduler.add_job(func=setting_job, trigger='interval', hours=24, timezone=pytz.utc)  #timezone=pytz.utc.dst
        scheduler.start()
    #return scheduler

# with appplication.app_context():
#     scheduler = BackgroundScheduler(jobstores=JOB_STORES)
#         #scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
#     scheduler.add_job(func=setting_job, trigger='interval', minutes=2, timezone=pytz.utc)  #timezone=pytz.utc.dst
#         #start the scheduler
#     scheduler.start()


if __name__ == "__main__":
    run_job()
    # scheduler = run_job()
    # scheduler.start()
    appplication.run(debug=True)
    