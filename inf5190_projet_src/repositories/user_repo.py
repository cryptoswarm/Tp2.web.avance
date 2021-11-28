from werkzeug.wrappers import response
from inf5190_projet_src import db
from inf5190_projet_src.models.user import User
from sqlalchemy import or_, and_, func, desc



def filter_by_username(username):
    user = User.query.filter_by(username=username).first()
    print('user for login in repository :',user)
    return user

def filter_by_email(email):
    user = User.query.filter_by(email=email).first()
    print('user found by email :',user)
    return user

def save_user(user):
    db.session.add(user)
    db.session.commit()
    user = filter_by_username(user.username)
    print('repository found user after creation :', user.id)
    return user.id

def filter_by_id(id):
    user_by_id = User.query.filter_by(id=id).first()
    print('user_by_id in repository: ',user_by_id)
    print('user_id in repository: ',user_by_id.id)
    return user_by_id