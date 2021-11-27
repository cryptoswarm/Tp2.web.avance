from inf5190_projet_src import db
from inf5190_projet_src.models.profile import Profile
from inf5190_projet_src.models.followed_arr import Followed


def find_profile_by_email(email:str)->Profile or None:
    profile = Profile.query.filter_by(email=email) \
                        .first()
    return profile

def save_profile(profile: Profile)->Profile:
    db.session.add(profile)
    db.session.commit()
    return profile


def save_followed_arr(name:str, profile_id:int):
    followed = Followed(name, profile_id)
    db.session.add(followed)
    db.session.commit()
    return followed

def find_followed_arr_by_name(name:str)->Followed or None:
    followed = Followed.query.filter_by(name=name) \
                        .first()
    return followed

def find_followed_by_profile_id(id:int):
    all = Followed.query.filter_by(profile_id=id) \
                        .all()
    return all