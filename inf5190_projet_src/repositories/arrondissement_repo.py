from werkzeug.wrappers import response
from inf5190_projet_src import db
from inf5190_projet_src.models.arrondissement import Arrondissement
from config import ARTICLES_PER_PAGE
from sqlalchemy import or_, and_, func, desc


def save_arrondissement(content):
    arrondissement = Arrondissement(content['nom_arr'], content['cle'])
    db.session.add(arrondissement)
    db.session.commit()
    print('arrondissement saved : ',arrondissement.asDictionary())
    return arrondissement

def find_by_arr_name(arr_name):
    return Arrondissement.query.filter_by(name=arr_name) \
                        .first()

# def get_id(nom_arr):
#     find_by_arr_name(nom_arr).id