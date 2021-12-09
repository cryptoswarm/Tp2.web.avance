import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler



# One of dev, prod or test
application = create_app('prod')

def setting_job_1():
    with application.app_context():
        application.logger.info('Starting patinoire scheduler')
        persist_patinoir_data()

def setting_job_2():
    with application.app_context():
        application.logger.info('Starting aqua scheduler')
        persist_aqua_data() 

def setting_job_3():
    with application.app_context():
        application.logger.info('Starting glissade scheduler')
        persist_glissade_data()


def setting_job_4():
    print('Print fct: This job is will run at 21h50 every day. time zone specified')


scheduler = BackgroundScheduler(daemon=True)
scheduler.start()
scheduler.add_job(setting_job_1, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_2, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_3, 'cron', hour=0, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(setting_job_4, 'cron', hour=21,  minute=50, timezone=pytz.timezone('CANADA/EASTERN'))


if __name__ == "__main__":
    application.run()
    
