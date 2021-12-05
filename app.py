import pytz
from inf5190_projet_src import create_app
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from flask_mail import Message
from inf5190_projet_src import mail


# One of dev, prod or test
application = create_app('prod')

if __name__ == "__main__":
    application.run()
    