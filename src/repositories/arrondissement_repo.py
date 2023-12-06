from src import db
from src.models.arrondissement import Arrondissement


def save_arrondissement(arrondissement):
    db.session.add(arrondissement)
    db.session.commit()
    return arrondissement


def find_by_arr_name(arr_name):
    response = Arrondissement.query.filter_by(name=arr_name).first()
    return response


def find_arr_by_id(arr_id):
    response = Arrondissement.query.filter_by(id=arr_id).first()
    return response
