# Define the app dir
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import pytz

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'inf5190_projet_src/static/files')

load_dotenv(os.path.join(BASE_DIR, '.env'))




# Generate an access token :
# curl -X GET "https://graph.facebook.com/oauth/access_token
#   ?client_id={your-app-id}
#   &client_secret={your-app-secret}
#   &grant_type=client_credentials"

#curl -X GET "https://graph.facebook.com/oauth/access_token?client_id=300878321886706&client_secret=3522525c38f6ece07ae317197da2fc24&grant_type=client_credentials"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Logging to stdout, useful when running heroku logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # unique ans secret key for signing the data
    CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')
    # JWT SECRET_KEY : import os then os.urandom(24)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # Silence 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Oauth credentials
    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': os.environ.get('FACEBOOK_CLIENT_ID'),
            'secret': os.environ.get('FACEBOOK_CLIENT_SECRET')
        },
        'twitter': {
            'id': os.environ.get('TWITTER_CLIENT_ID'),
            'secret': os.environ.get('TWITTER_CLIENT_SECRET')
        }
    }
    DEBUG = False
    ADMIN_USERNAME= os.environ.get('APP_ADMIN_USERNAME')
    ADMIN_PASS = os.environ.get('APP_ADMIN_PASS')
    ADMIN_ID = os.environ.get('APP_ADMIN_ID')
    MAIL_SERVER =  'smtp.gmail.com'
    MAIL_PORT =  465
    # MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    DATA_SWARM_MAIL_SUBJECT_PREFIX = ''
    DATA_SWARM_MAIL_SENDER = ''
    UNSUBSCRIBE_LINK = ''
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax"
    

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    JOB_STORE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'jobs.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOB_STORES = {
        'default': SQLAlchemyJobStore(JOB_STORE_URL)
    }
    EXECUTORS= {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    JOB_DEFAULTS= {
        'coalesce': True,
        'max_instances': 3
    }
    UNSUBSCRIBE_LINK = 'http://localhost:4200/unsubscribe/'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app_test.db')
    JOB_STORE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'jobs_test.sqlite')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOB_STORES = {
        'default': SQLAlchemyJobStore(JOB_STORE_URL)
    }
    EXECUTORS= {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    JOB_DEFAULTS= {
        'coalesce': True,
        'max_instances': 3
    }


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    DATABASE_URL= os.environ.get('DATABASE_URL_BASIC')
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    JOB_STORES = {
        'default': SQLAlchemyJobStore(DATABASE_URL)
    }
    EXECUTORS= {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    JOB_DEFAULTS= {
        'coalesce': True,
        'max_instances': 3
    }
    UNSUBSCRIBE_LINK = 'https://data-swarm.herokuapp.com/unsubscribe/'
    


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
JWT = Config.JWT_SECRET_KEY
USERNAME = Config.ADMIN_USERNAME
PASSWORD = Config.ADMIN_PASS
ADMIN_ID = Config.ADMIN_ID
UNSUBSCRIBE = Config.UNSUBSCRIBE_LINK