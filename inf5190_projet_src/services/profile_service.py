from inf5190_projet_src.repositories.profile_repo import *


def remove_profile(profile: Profile):
    deleted_profile = delete_profile(profile.email, profile.id)
    return deleted_profile


def add_profile(data):
    profile = Profile(data['complete_name'], data['email'])
    profile = save_profile(profile)
    return profile


def get_profile_by_email(email: str):
    profile = find_profile_by_email(email)
    if profile is None:
        return None, 404
    return profile, 200


def create_profile_followed_arr(data):
    content = []
    followed_arron = data['followed_arr']
    email = data['email']
    profile, code = get_profile_by_email(email)
    if profile is None:
        profile = add_profile(data)
    for name in followed_arron:
        existed_arr = find_followed_arr_name_id(name, profile.id)
        if existed_arr is None:
            save_followed_arr(name, profile.id)
    response = profile.asDictionary()
    items = find_followed_by_profile_id(profile.id)
    for item in items:
        content.append(item.asDictionary())
    response['followed_arr'] = content
    return response
