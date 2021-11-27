from inf5190_projet_src.repositories.bl_token_repo import *

def save_bk_token(auth_token):
    print('Saving token started in bk_listed service:', auth_token)
    blacklist_token = add_bk_token(auth_token)
    return blacklist_token