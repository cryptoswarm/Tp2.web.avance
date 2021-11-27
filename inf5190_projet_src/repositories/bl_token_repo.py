
from inf5190_projet_src import db
from inf5190_projet_src.models.black_listed import BlacklistToken


def add_bk_token(auth_token):
    blacklist_token = BlacklistToken(auth_token)
    # insert the token
    print('Saving bk token started successfully in bk_listed token repo')
    db.session.add(blacklist_token)
    db.session.commit()
    print('Saving bk token ended successfully in bk_listed token repo')
    return blacklist_token