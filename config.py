# Define the app dir
import os
from dotenv import load_dotenv


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Enable the dev env
DEBUG = True



# Define the db
# SQLite for the current app or postgresql
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
#         'postgres://', 'postgresql://') or \
#         'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

DATABASE_CONNECT_OPTIONS = {}


# unique ans secret key for signing the data
CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')

# Secret key for signing cookies

COOKIES_SIGNIN_SECRET_KEY = os.environ.get('COOKIES_SIGNIN_SECRET_KEY')

# Silence 
SQLALCHEMY_TRACK_MODIFICATIONS = False

# number of articles per page
ARTICLES_PER_PAGE = 5

# JWT SECRET_KEY : import os then os.urandom(24)
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

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

# Generate an access token :
# curl -X GET "https://graph.facebook.com/oauth/access_token
#   ?client_id={your-app-id}
#   &client_secret={your-app-secret}
#   &grant_type=client_credentials"

#curl -X GET "https://graph.facebook.com/oauth/access_token?client_id=300878321886706&client_secret=3522525c38f6ece07ae317197da2fc24&grant_type=client_credentials"

# Logging to stdout, useful when running heroku logs
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

# Upload folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'inf5190_projet_src/static/files')