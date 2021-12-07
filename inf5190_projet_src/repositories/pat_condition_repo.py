
from flask_sqlalchemy import Pagination
from sqlalchemy.sql.expression import extract
from inf5190_projet_src import db
from inf5190_projet_src.models.patinoir_condition import PatinoirCondition
from sqlalchemy import or_, and_, func, desc


def save_pat_condition(pat_condition):
    print('pat_condition received :',pat_condition.asDictionary())
    db.session.add(pat_condition)
    db.session.commit()
    print(print('pat_condition created :',pat_condition.asDictionary()))
    return pat_condition

def find_pat_conditions_by_pat_id(pat_id):
    return PatinoirCondition.query.filter_by(patinoire_id=pat_id).all()

def find_pat_condition_cond_id(condition_id):
    return PatinoirCondition.query.filter_by(id=condition_id).first()

def update_patinoire_condition(existed, updated_data):
    existed.arrose = updated_data['arrose']
    existed.date_heure = updated_data['date_heure']
    existed.deblaye = updated_data['deblaye']
    existed.ouvert = updated_data['ouvert']
    existed.resurface = updated_data['resurface']
    db.session.commit()
    return existed

def delete_condition(condition_id):
    condition = find_pat_condition_cond_id(condition_id)
    db.session.delete(condition)
    db.session.commit()
    return condition

def find_pat_cond_by_hash(hash):
    return PatinoirCondition.query.filter_by(pat_hash = hash).first()

def find_pat_conditions_by_year(year):
    conditions = db.session.query(PatinoirCondition).filter(extract('year', PatinoirCondition.date_heure)==year).all()
    return conditions

def find_pat_ids_from_conditions_by_year(year):
    ids = PatinoirCondition \
            .query.with_entities(PatinoirCondition.patinoire_id) \
            .filter(extract('year', PatinoirCondition.date_heure)==year) \
            .distinct().all()
    print('ids = ', ids)
    return ids
