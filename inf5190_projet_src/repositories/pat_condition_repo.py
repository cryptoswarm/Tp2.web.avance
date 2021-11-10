
from flask_sqlalchemy import Pagination
from inf5190_projet_src import db
from inf5190_projet_src.models.patinoir_condition import PatinoirCondition
from sqlalchemy import or_, and_, func, desc


def save_pat_condition(pat_condition):
    # pat_condition = PatinoirCondition(content['date_heure'],
    #                                   content['ouvert'],
    #                                   content['deblaye'],
    #                                   content['arrose'],
    #                                   content['resurface'],
    #                                   content['patinoire_id'])
    print('pat_condition received :',pat_condition.asDictionary())
    db.session.add(pat_condition)
    db.session.commit()
    print(print('pat_condition created :',pat_condition.asDictionary()))
    return pat_condition

# def find_patinoire_by_name(nom_pat):
#     return Patinoire.query.filter_by(nom_pat=nom_pat) \
#                         .first()

    # db.session.add(patinoire)
    # db.session.commit()