import logging

from sqlalchemy.sql.expression import extract
from inf5190_projet_src import db
from inf5190_projet_src.models.glissade import Glissade
from sqlalchemy import or_, and_, func, desc


def save_glissade(glissade):
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

def find_glissades_names_arr_id(arr_id):
    return Glissade.query.with_entities(Glissade.name, Glissade.id) \
                   .filter_by(arrondissement_id=arr_id) \
                   .all()

def find_glissades_by_year(year):
    # return Glissade.query.filter_by(date_maj=year).all()
    glissades = db.session.query(Glissade).filter(extract('year', Glissade.date_maj)==year).all()
    for glis in glissades:
        logging.info('glissade: ', glis.asDictionary())
        print('glissade: ', glis.asDictionary())
    return glissades

def find_glissade_by_id(glissade_id):
    return Glissade.query.filter_by(id=glissade_id).first()

def update(glissade, posted_glissade):
    glissade.date_maj = posted_glissade['date_maj']
    glissade.ouvert = posted_glissade['ouvert']
    glissade.deblaye =  posted_glissade['deblaye']
    glissade.condition = posted_glissade['condition']
    db.session.commit()
    return glissade

def delete_by_id(id):
    glissade = find_glissade_by_id(id)
    db.session.delete(glissade)
    db.session.commit()
    return glissade

def find_glissade_details(arr_id, glissade_name):
    glissade = Glissade \
           .query \
           .filter(and_(
               (Glissade.arrondissement_id == arr_id), 
               (Glissade.name == glissade_name)
               )).first()
    print('Glissade :', glissade)
    logging.info('Glissade: ', glissade)
    return glissade