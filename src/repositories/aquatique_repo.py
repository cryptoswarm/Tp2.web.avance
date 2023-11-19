import logging
from inf5190_projet_src import db
from inf5190_projet_src.models.inst_aquatique import InstallationAquatique
from sqlalchemy import and_


def save_installation_aquatique(aquatique_insta):
    db.session.add(aquatique_insta)
    db.session.commit()
    return aquatique_insta


def find_all_aqua_installation_by_arr_id(arr_id):
    return InstallationAquatique.query.filter_by(arron_id=arr_id).all()


def find_aqua_insta_by_hash(hash):
    return InstallationAquatique.query.filter_by(aqua_hash=hash).first()


def find_aqua_by_id(id):
    return InstallationAquatique.query.filter_by(id=id).first()


def update_aqua(id, data):
    to_be_updated = find_aqua_by_id(id)
    to_be_updated.nom_installation = data['nom_installation']
    to_be_updated.type_installation = data['type_installation']
    to_be_updated.adress = data['adress']
    to_be_updated.propriete_installation = data['propriete_installation']
    to_be_updated.gestion_inst = data['gestion_inst']
    to_be_updated.equipement_inst = data['equipement_inst']
    to_be_updated.aqua_hash = to_be_updated.calculate_hash()
    logging.info('Recalc hash : {}'.format(to_be_updated.aqua_hash))
    db.session.commit()
    return to_be_updated


def find_aqua_inst_names_arr_id(arr_id):
    return InstallationAquatique \
           .query \
           .with_entities(InstallationAquatique.nom_installation,
                          InstallationAquatique.id) \
           .filter_by(arron_id=arr_id).all()


def find_aqua_installations(arr_id, aqua_name):
    response = InstallationAquatique \
           .query \
           .filter(and_(
               (InstallationAquatique.arron_id == arr_id),
               (InstallationAquatique.nom_installation == aqua_name)
               )).all()
    return response


def delete_aqua_by_id(id):
    aqua = find_aqua_by_id(id)
    db.session.delete(aqua)
    db.session.commit()
    return aqua
