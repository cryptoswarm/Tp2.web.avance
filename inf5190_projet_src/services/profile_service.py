import re

from werkzeug.wrappers import response
from inf5190_projet_src.repositories.profile_repo import *

def add_profile(data):
    profile = Profile(data['complete_name'], data['email'])
    profile = save_profile(profile)
    return profile

def get_profile_by_email(email:str):
    profile = find_profile_by_email(email)
    if profile is None:
        return None, 404
    return profile, 200

def create_profile_followed_arr(data):
    content = []
    followed_arron = data['followed_arr']
    email = data['email']
    for name in followed_arron:
        profile, status = get_profile_by_email(email)
        if profile is None:
            profile = add_profile(data)
        existed_arr = find_followed_arr_by_name(name)
        if existed_arr is None:
            print('name',name, 'profile.id', profile.id)
            save_followed_arr(name, profile.id)
    
    response = {"name": profile.complete_name,
                "email": profile.email,
                }
    items = find_followed_by_profile_id(profile.id)
    for item in items:
        content.append(item.asDictionary())
    response['followed_arr'] = content
    return response



