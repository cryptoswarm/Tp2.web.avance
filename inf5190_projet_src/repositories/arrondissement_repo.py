from werkzeug.wrappers import response
from inf5190_projet_src import db
from inf5190_projet_src.models.arrondissement import Arrondissement
from config import ARTICLES_PER_PAGE
from sqlalchemy import or_, and_, func, desc


def save_arrondissement(arrondissement):
    #arrondissement = Arrondissement(content['nom_arr'], content['cle'])
    db.session.add(arrondissement)
    db.session.commit()
    print('arrondissement saved : ',arrondissement.asDictionary())
    return arrondissement

def find_by_arr_name(arr_name):
    print('cheking existence of arrondissement: {}'.format(arr_name))
    response =  Arrondissement.query.filter_by(name=arr_name) \
                        .first()
    if response is None:
        print('Arrondissement {} does not exist'.format(arr_name))
    else:
        print('Arrondissement {} exist!'.format(arr_name))
    return response

def find_arr_by_id(arr_id):
    response =  Arrondissement.query.filter_by(id=arr_id) \
                        .first()
    return response
