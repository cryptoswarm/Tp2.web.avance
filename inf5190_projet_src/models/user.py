from app import db
import jwt
from datetime import datetime, timedelta
from config import JWT
from inf5190_projet_src.models.black_listed import BlacklistToken

# Define the base model


class Base(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class User(Base):
    __tablename__ = 'user'  

    # email of user
    email = db.Column(db.String(100), unique=True,  nullable=False)

    # username of user
    username = db.Column(db.String(100), unique=True,  nullable=False)
    # password of user
    hashed_pass = db.Column(db.String(255), nullable=False)
    # salt used for hashing the password
    salt = db.Column(db.String(255), unique=True,  nullable=False)
    # User role
    admin = db.Column(db.Boolean, nullable=False, default=False)
    # Registration time
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, username, hashed_pass, salt, admin=False):
        self.email = email
        self.username = username
        self.hashed_pass = hashed_pass
        self.salt = salt
        self.admin = admin
        self.registered_on = datetime.now()


    def __repr__(self):
        return "<User(user_id='%d', email='%s', username='%s', hashed_pass='%s', salt='%s', admin='%s')>" % (
            self.id, self.email, self.username, self.hashed_pass, self.salt, self.admin)

    def asDictionary(self):
        return {"user_id": self.id,
                "email":self.email,
                "username": self.username,
                "hashed_pass": self.hashed_pass,
                "salt": self.salt,
                "admin": self.admin
                }
    @staticmethod
    def encode_auth_token(user_id):
        """Generates the Auth Token:return: string"""
        try:
            payload = {
                # Expiration Time claim : expire after 30 min = 1800 sec
                'exp': datetime.utcnow() + timedelta(days=0, seconds=1800),
                # Issued At claim
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                JWT,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, JWT, 'HS256')
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            print('Will expire at :',payload['exp'])
            print('user_id = payload[sub] :',payload['sub'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'