# Define the app dir
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "src/static/files")

load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Logging to stdout, useful when running heroku logs
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    # unique ans secret key for signing the data
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")
    # Silence
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    ADMIN_USERNAME = os.environ.get("APP_ADMIN_USERNAME")
    ADMIN_PASS = os.environ.get("APP_ADMIN_PASS")
    ADMIN_ID = os.environ.get("APP_ADMIN_ID")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = (True,)
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    DATA_SWARM_MAIL_SUBJECT_PREFIX = ""
    DATA_SWARM_MAIL_SENDER = ""
    UNSUBSCRIBE_LINK = ""
    SESSION_COOKIE_HTTPONLY = (True,)
    REMEMBER_COOKIE_HTTPONLY = (True,)
    SESSION_COOKIE_SAMESITE = "Lax"


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    if not os.path.exists("db"):
        os.mkdir("db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db/app.db")
    JOB_STORE_URL = "sqlite:///" + os.path.join(BASE_DIR, "db/jobs.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #  'http://localhost:4200/unsubscribe/'
    # Pour pouvoire tester en utilisant vagrant
    UNSUBSCRIBE_LINK = "http://172.28.128.8:5000/unsubscribe/"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    if not os.path.exists("db"):
        os.mkdir("db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db/app_test.db")
    JOB_STORE_URL = "sqlite:///" + os.path.join(BASE_DIR, "db/jobs_test.sqlite")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    DATABASE_URL = os.environ.get("DATABASE_URL_BASIC")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    UNSUBSCRIBE_LINK = "https://data-swarm.herokuapp.com/unsubscribe/"


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
USERNAME = Config.ADMIN_USERNAME
PASSWORD = Config.ADMIN_PASS
ADMIN_ID = Config.ADMIN_ID
UNSUBSCRIBE = Config.UNSUBSCRIBE_LINK
