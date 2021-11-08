from inf5190_projet_src import db
from inf5190_projet_src.models.glissade import Glissade
from sqlalchemy import or_, and_, func, desc


def save_glissade(content):
    glissade = Glissade(content['name'], content['date_maj'], 
                              content['ouvert'], content['deblaye'],
                              content['condition'], content['arrondissement_id'])
    print('glissade :',glissade.asDictionary())
    db.session.add(glissade)
    db.session.commit()
    return glissade

def find_glissade_by_name(glissade_name):
    return Glissade.query.filter_by(name=glissade_name) \
                        .first()