import csv, sys
from re import escape
from operator import pos
from config import UPLOAD_FOLDER
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.models.piscines_aquatique import InstallationAquatique
from inf5190_projet_src.models.coordiante import Coordiante
from inf5190_projet_src.repositories.coordiantes_repo import *
from inf5190_projet_src.repositories.aquatique_repo import *

def read_and_save_data_from_csv_file(file_name):
    holder = []
    path_to_file = UPLOAD_FOLDER+'/{}'.format(file_name)
    with open(path_to_file, 'r') as file:
        #reader = csv.reader(file, delimiter=',', doublequote=False) #encoding='utf-8' escapechar='"'
        reader = csv.reader(file, quotechar='"')
        headers = next(reader, None) # skip the headers
        try:
            for row in reader:
                print('row: ',row)
                arr_id = None
                position_id = None
                arron_name = row[3]
                arrondissement = find_by_arr_name(arron_name)
                if  arrondissement is None:
                    arrondissement = save_arrondissement({'nom_arr': arron_name, 'cle': None})
                    arr_id = arrondissement.id
                arr_id = arrondissement.id
                position = construct_aqua_position(row)
                created_pos = save_inst_aquatique_position(position)
                position_id = created_pos.id
                aqua_inst = construct_new_inst_aquatique(row)
                aqua_inst.arron_id = arr_id
                aqua_inst.position_id = position_id
                created_aqua_int = save_installation_aquatique(aqua_inst)
                display_created_aqua_inst(holder, arrondissement, created_pos, created_aqua_int)
            return holder
        except csv.Error as e:
            return('file {}, line {}: {}'.format(file_name, reader.line_num, e))
            #sys.exit()

def construct_new_inst_aquatique(data):
    inst_aqua = InstallationAquatique(None, None, None, None, None, None, None, None)
    inst_aqua.type_installation = data[1]
    inst_aqua.nom_installation = data[2]
    inst_aqua.adress = data[4]
    inst_aqua.propriete_installation =  data[5]
    inst_aqua.gestion_inst = data[6]
    inst_aqua.equipement_inst = data[9]
    return inst_aqua

def construct_aqua_position(data):
    position = Coordiante(None, None, None, None)
    position.point_x = data[7]
    position.point_y = data[8]
    position.longitude = data[10]
    position.latitude = data[11]
    return position

def display_created_aqua_inst(holder, arron, created_pos, created_aqua_int):
    holder.append(arron.asDictionary())
    holder.append(created_pos.asDictionary())
    holder.append(created_aqua_int.asDictionary())
