from operator import and_
from inf5190_projet_src import db
from inf5190_projet_src.models.profile import Profile
from inf5190_projet_src.models.followed_arr import InspectedArr


def delete_profile(email, profile_id):
    followed_arr = InspectedArr.query \
                               .filter_by(profile_id=profile_id) \
                               .delete()
    profile = Profile.query \
                     .filter_by(email=email) \
                     .delete()
    db.session.commit()
    return profile, followed_arr


def find_profile_by_email(email: str) -> Profile or None:
    profile = Profile.query.filter_by(email=email) \
                        .first()
    return profile


def save_profile(profile: Profile) -> Profile:
    db.session.add(profile)
    db.session.commit()
    return profile


def save_followed_arr(name: str, profile_id: int):
    followed = InspectedArr(name, profile_id)
    db.session.add(followed)
    db.session.commit()
    return followed


def find_followed_arr_by_name(name: str) -> InspectedArr or None:
    return InspectedArr.query \
                           .filter_by(name=name) \
                           .first()


def find_followed_by_profile_id(id: int):
    return InspectedArr.query \
                       .filter_by(profile_id=id) \
                       .all()


def find_followed_arr_name_id(name: str, id: int) -> InspectedArr or None:
    return InspectedArr.query \
                       .filter(and_(
                                    (InspectedArr.name == name),
                                    (InspectedArr.profile_id == id)
                                )).first()
