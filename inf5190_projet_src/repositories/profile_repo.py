from operator import and_
from inf5190_projet_src import db
from inf5190_projet_src.models.profile import Profile
from inf5190_projet_src.models.followed_arr import InspectedArr

def delete_profile(email):
    profile = find_profile_by_email(email)
    db.session.delete(profile)
    db.session.commit

def delete_followed_arr_by_profile_id(profile_id):
    arrs = find_followed_by_profile_id(profile_id)
    for arr in arrs:
        db.session.delete(arr)
        db.session.commit()

def find_profile_by_email(email:str)->Profile or None:
    profile = Profile.query.filter_by(email=email) \
                        .first()
    return profile

def save_profile(profile: Profile)->Profile:
    db.session.add(profile)
    db.session.commit()
    return profile


def save_followed_arr(name:str, profile_id:int):
    followed = InspectedArr(name, profile_id)
    db.session.add(followed)
    db.session.commit()
    return followed

def find_followed_arr_by_name(name:str)->InspectedArr or None:
    followed = InspectedArr.query.filter_by(name=name) \
                        .first()
    return followed

def find_followed_by_profile_id(id:int):
    all = InspectedArr.query.filter_by(profile_id=id) \
                        .all()
    return all

def find_followed_arr_name_id(name:str, profile_id:int)->InspectedArr or None:
    followed = InspectedArr \
               .query \
               .filter(and_(
                   (InspectedArr.name==name),
                   (InspectedArr.profile_id==profile_id)
                   )).first()
    return followed

