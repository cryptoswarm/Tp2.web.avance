from werkzeug.wrappers import response
from inf5190_projet_src import db
from inf5190_projet_src.models.arrondissement import Arrondissement
from sqlalchemy import or_, and_, func, desc


def save_arrondissement(arrondissement):
    db.session.add(arrondissement)
    db.session.commit()
    return arrondissement

def find_by_arr_name(arr_name):
    response =  Arrondissement.query.filter_by(name=arr_name) \
                        .first()
    return response

def find_arr_by_id(arr_id):
    response =  Arrondissement.query.filter_by(id=arr_id) \
                        .first()
    return response
