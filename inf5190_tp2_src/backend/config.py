# Define the app dir
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable the dev env
DEBUG = True



# Define the db
# SQLite for the current app
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}


# unique ans secret key for signing the data
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies

SECRET_KEY = "secret"

# Silence 
SQLALCHEMY_TRACK_MODIFICATIONS = False

# number of articles per page
ARTICLES_PER_PAGE = 5

# JWT SECRET_KEY : import os then os.urandom(24)
JWT_SECRET_KEY = ""

# Oauth credentials
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '300878321886706',
        'secret': '3522525c38f6ece07ae317197da2fc24'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}

# Generate an access token :
# curl -X GET "https://graph.facebook.com/oauth/access_token
#   ?client_id={your-app-id}
#   &client_secret={your-app-secret}
#   &grant_type=client_credentials"