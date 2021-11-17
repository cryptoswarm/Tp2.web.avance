from inf5190_projet_src import db
from inf5190_projet_src.models.glissade import Glissade
from sqlalchemy import or_, and_, func, desc


def save_glissade(glissade):
    # glissade = Glissade(content['name'], content['date_maj'], 
    #                           content['ouvert'], content['deblaye'],
    #                           content['condition'], content['arrondissement_id'])
    print('Received glissade :',glissade.asDictionary())
    db.session.add(glissade)
    db.session.commit()
    print('Created glissade :',glissade.asDictionary())
    return glissade

def find_glissade_by_name(glissade_name):
    return Glissade.query.filter_by(name=glissade_name) \
                        .first()

def find_all_glissades_by_arr_id(arr_id):
    return Glissade.query.filter_by(arrondissement_id=arr_id).all()

def find_glissade_by_id(glissade_id):
    return Glissade.query.filter_by(id=glissade_id).first()