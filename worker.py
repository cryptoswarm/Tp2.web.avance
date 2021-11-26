import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *



app = create_app('prod')

if app.config['LOG_TO_STDOUT']:
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


def setting_job_1():
    with app.app_context():
        app.logger.info('Starting patinoire scheduler')
        persist_patinoir_data()

def setting_job_2():
    with app.app_context():
        app.logger.info('Starting aqua scheduler')
        persist_aqua_data() 

def setting_job_3():
    with app.app_context():
        app.logger.info('Starting glissade scheduler')
        persist_glissade_data()

def setting_job_4():
    with app.app_context():
        print('Print fct: This job is run every 1 min. utc time')
        app.logger.info('Logger fct: This job is run every 1 min. utc time')

def setting_job_5():
    with app.app_context():
        print('Print fct: This job is run every 2 min. canada/easter')
        app.logger.info('This job is run every 2 min. canada/easter')

# def start_working():
#     scheduler = BackgroundScheduler(jobstores=app.config['JOB_STORES'], job_defaults=app.config['JOB_DEFAULTS'])
#     scheduler.start()

#     #scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
#     #scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.timezone('CANADA/EASTERN'))
#     #scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.utc)
#     # scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
#     # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=5, timezone=pytz.utc)
#     # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=1, timezone=pytz.timezone('CANADA/EASTERN'))
#     # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=1, timezone=pytz.utc)
#     scheduler.add_job(func=setting_job_4, trigger='interval', minutes=1, timezone=pytz.utc)
#     scheduler.add_job(func=setting_job_5, trigger='interval', minutes=2, timezone=pytz.timezone('CANADA/EASTERN'))
    

# if __name__ == '__main__':
#     start_working()


scheduler = BackgroundScheduler(jobstores=app.config['JOB_STORES'], job_defaults=app.config['JOB_DEFAULTS'])


    #scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
    #scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.timezone('CANADA/EASTERN'))
    #scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.utc)
    # scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
    # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=5, timezone=pytz.utc)
    # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=1, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(func=setting_job_3, trigger='interval', minutes=10, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.add_job(func=setting_job_3, trigger='interval', minutes=5, timezone=pytz.utc)
scheduler.add_job(func=setting_job_4, trigger='interval', minutes=1, timezone=pytz.utc)
scheduler.add_job(func=setting_job_5, trigger='interval', minutes=2, timezone=pytz.timezone('CANADA/EASTERN'))
scheduler.start()




