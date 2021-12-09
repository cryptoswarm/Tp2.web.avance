import csv
import logging
from requests.models import Response
from inf5190_projet_src.models.inst_aquatique import \
    InstAquatiquePosition, InstallationAquatique
from inf5190_projet_src.repositories.aquatique_repo import *
from inf5190_projet_src.services.coordinate_service import \
    get_position_by_id


def construct_new_inst_aquatique(data) -> InstallationAquatique:
    nom_inst = data[2]
    type_inst = data[1]
    adress = data[4]
    propriete_inst = data[5]
    gestion_inst = data[6]
    equipement_inst = data[9]
    inst_aqua = InstallationAquatique(nom_inst, type_inst,
                                      adress, propriete_inst,
                                      gestion_inst,
                                      equipement_inst, None, None)
    return inst_aqua


def get_all_aqua_installation_by_arr_id(arr_id):
    all_aqua_inst = []
    installations = find_all_aqua_installation_by_arr_id(arr_id)
    if installations is None:
        logging.debug('Aqua inst by arr id : {} not found'.format(arr_id))
        return {}, 404
    for installation in installations:
        position = get_position_by_id(installation.position_id)
        inst = installation.asDictionary()
        inst['position'] = position.asDictionary()
        all_aqua_inst.append(inst)
    return all_aqua_inst, 200


def get_aqua_inst_by_hash(hash):
    installation = find_aqua_insta_by_hash(hash)
    if installation is None:
        return None
    return installation


def get_aqua_inst_by_id(id):
    installation = find_aqua_by_id(id)
    if installation is None:
        return None, 404
    return installation, 200


def update_aqua_inst(id, data):
    updated_aqua = update_aqua(id, data)
    return updated_aqua, 200


def delete_aqua_inst_by_id(id):
    deleted_aqua = delete_aqua_by_id(id)
    return deleted_aqua


def get_aqua_inst_names_arr_id(arr_id):
    response = []
    aqua_inst_names = find_aqua_inst_names_arr_id(arr_id)
    if aqua_inst_names is None:
        logging.debug('Names aqua inst arr id : {} not found'.format(arr_id))
        return None
    for aqua in aqua_inst_names:
        response.append({'id': aqua[1], 'nom_installation': aqua[0]})
    return response


def get_aqua_installations(arrond_id, aqua_name):
    response = []
    aqua_inst = find_aqua_installations(arrond_id, aqua_name)
    if len(aqua_inst) == 0:
        return None
    for aqua in aqua_inst:
        position = get_position_by_id(aqua.position_id)
        if position is not None:
            inst_pos = InstAquatiquePosition(aqua.id, aqua.nom_installation,
                                             aqua.type_installation,
                                             aqua.adress,
                                             aqua.propriete_installation,
                                             aqua.gestion_inst,
                                             aqua.equipement_inst,
                                             aqua.arron_id,
                                             aqua.position_id, position)
            response.append(inst_pos)
    return response


def add_installation_aquatique(aqua_inst: InstallationAquatique):
    new_aqua = save_installation_aquatique(aqua_inst)
    return new_aqua
