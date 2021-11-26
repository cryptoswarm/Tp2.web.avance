import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *



app = create_app('prod')

def setting_job_1():
    with app.app_context():
        persist_patinoir_data()

def setting_job_2():
    with app.app_context():
        persist_aqua_data() 

def setting_job_3():
    with app.app_context():
        persist_glissade_data()

def start_working():
    scheduler = BackgroundScheduler(jobstores=app.config['JOB_STORES'], job_defaults=app.config['JOB_DEFAULTS'])
    

    #scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
    scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.timezone('CANADA/EASTERN'))
    #scheduler.add_job(func=setting_job_1, trigger='interval', minutes=5, timezone=pytz.utc)
    # scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
    # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=5, timezone=pytz.utc)
    # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=1, timezone=pytz.timezone('CANADA/EASTERN'))
    # scheduler.add_job(func=setting_job_3, trigger='interval', minutes=1, timezone=pytz.utc)
    scheduler.start()
if __name__ == '__main__':
    start_working()






