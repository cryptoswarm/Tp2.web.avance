import pytz
# from inf5190_projet_src import create_app
from inf5190_projet_src import application
from inf5190_projet_src.controllers.data_requester import *
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

# application = create_app()



if __name__ == "__main__":
    application.run(debug=True)
    