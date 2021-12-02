import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler
import time



app = create_app('prod')

# if app.config['LOG_TO_STDOUT']:
#     handler = logging.StreamHandler()
#     handler.setLevel(logging.INFO)
#     app.logger.addHandler(handler)


def setting_job_1():
    with app.app_context():
        print('Patinoire scheduler is triggered')
        app.logger.info('Starting patinoire scheduler')
        persist_patinoir_data()

def setting_job_2():
    with app.app_context():
        print('Aqua scheduler is triggered')
        app.logger.info('Starting aqua scheduler')
        persist_aqua_data() 

def setting_job_3():
    with app.app_context():
        print('Glissade scheduler is triggered')
        app.logger.info('Starting glissade scheduler')
        persist_glissade_data()


def setting_job_4():
    # with app.app_context():
    print('Print fct: This job is run every 5 min. no time zone specified')



scheduler = BackgroundScheduler()
scheduler.add_job(setting_job_1, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_2, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_3, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_4, 'interval', minutes=5, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.start()

if __name__ == "__main__":
    while True:
        print('next wake up time in 5 minutes')
        scheduler.print_jobs()
        time.sleep(280)
