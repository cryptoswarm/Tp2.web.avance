import xmltodict
import xml.etree.ElementTree as ET
from threading import Condition
from datetime import datetime
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.repositories.glissade_repo import *
from inf5190_projet_src.repositories.patinoire_repo import find_patinoire_by_name, save_patinoire
from inf5190_projet_src.repositories.pat_condition_repo import *
from inf5190_projet_src.models.patinoir_condition import PatinoirCondition
from inf5190_projet_src.models.patinoire import Patinoire


def write_response_to_file(response, file_name):
    with open(file_name, 'w') as file:
        for line in response:
            file.write(line)


def get_arrondissement_detail(arr_details):
    nom_arr = arr_details['nom_arr']
    cle = arr_details['cle']
    date_maj = datetime.strptime(arr_details['date_maj'], "%Y-%m-%d %H:%M:%S")
    return {'nom_arr':nom_arr, 'cle':cle, 'date_maj': date_maj}

def get_glissade_details(element, kwargs):
    glissade_name = element[kwargs[0][0]]
    print('type of element[kwargs[0][2]] :', type(element[kwargs[0][2]]))
    ouvert = False if element[kwargs[0][2]] == '0' else True
    deblaye = False if element[kwargs[0][3]] == '0' else True
    condition = element[kwargs[0][4]]
    return {'name':glissade_name, 'ouvert':ouvert, 'deblaye':deblaye, 'condition':condition}


#'MAIN', 'arrondissement', ['nom_arr', 'patinoire']
def get_patinoire_details(details):
    pat_conditions = {}
    cond_list = []
    nom_pat = details['patinoire']['nom_pat']
    pat_conditions['nom_pat'] = nom_pat
    print('Building patinoire conditions :', nom_pat)
    conditions = details['condition']
    for condition in conditions:
        date_heure =  condition['date_heure']
        ouvert = False if condition['ouvert'] == 0 else True
        deblaye = False if condition['deblaye'] == 0 else True
        arrose = False if condition['arrose'] == 0 else True
        resurface = False if condition['resurface'] == 0 else True
        condition = {'date_heure':date_heure,
                     'ouvert': ouvert, 'deblaye':deblaye,
                     'arrose':arrose, 'resurface':resurface}
        cond_list.append(condition)
    pat_conditions['conditions'] = cond_list
    return pat_conditions


def save_pat_and_conditions(patinoire_xml):
    content = []
    with open(patinoire_xml, 'r') as file:
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root: #child.tag #<---- list of all arrondissements
            nom_arr = child.find('nom_arr').text.strip()
            arrondissement= find_by_arr_name(nom_arr)
            if arrondissement is None:
                to_be_created = Arrondissement(nom_arr, None)
                arrondissement = save_arrondissement(to_be_created)
                content.append(arrondissement.asDictionary())
            patinoire_elem = child.find('patinoire')
            for children in patinoire_elem:
                if children.tag == 'nom_pat':
                    nom_pat = children.text.strip()
                    patinoire = find_patinoire_by_name(nom_pat)
                    if patinoire is None:
                        patinoire = Patinoire(nom_pat, arrondissement.id)
                        new_pat = save_patinoire(patinoire)
                        content.append(new_pat.asDictionary())
                if children.tag == 'condition':
                    pat_cond = get_patinoire_condition(children)
                    pat_id =  find_patinoire_by_name(nom_pat).id
                    pat_cond.patinoire_id = pat_id
                    saved_condition = save_pat_condition(pat_cond)
                    content.append(saved_condition.asDictionary())
        return content


def save_all_glissade(glissade_xml):
    content = []
    with open(glissade_xml, 'r') as file:
        tree = ET.parse(file)
        root = tree.getroot()
        for glissade_elm in root:
            arrondissement = get_arrondissement(glissade_elm)
            checked_arr = find_by_arr_name(arrondissement.name)
            if checked_arr is None:
                checked_arr = save_arrondissement(arrondissement)
            content.append(checked_arr.asDictionary())
            glissade = get_glissade(glissade_elm)
            glissade.arrondissement_id = checked_arr.id
            checked_glissade = find_glissade_by_name(glissade.name)
            if checked_glissade is None:
                glissade = save_glissade(glissade)
            content.append(glissade.asDictionary())
    return content

def get_arrondissement(glissade_elem):
    arr_elem = glissade_elem.find('arrondissement')
    name = arr_elem.find('nom_arr').text
    cle = arr_elem.find('cle').text
    return Arrondissement(name, cle)

def get_glissade(glissade_elem):
    date_text = glissade_elem.find('arrondissement').find('date_maj').text
    date_maj = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")
    name = glissade_elem.find('nom').text
    ouvert = False if glissade_elem.find('ouvert').text == '0' else True 
    deblaye = False if glissade_elem.find('deblaye').text == '0' else True 
    condition = glissade_elem.find('condition').text
    return Glissade(name, date_maj, ouvert, deblaye, condition, None)

def get_patinoire_condition(pat_content):
    date_heure = datetime.strptime(pat_content.find('date_heure').text.strip(), "%Y-%m-%d %H:%M:%S")
    ouvert = True if pat_content.find('ouvert').text.strip() == '1' else False 
    deblaye = True if pat_content.find('deblaye').text.strip() == '1' else False #children.find('deblaye')
    arrose = True if pat_content.find('arrose').text.strip() == '1' else False #children.find('arrose')
    resurface = True if pat_content.find('resurface').text.strip() == '1' else False #children.find('resurface')
    return PatinoirCondition(date_heure, ouvert, deblaye, arrose, resurface, None)


def get_glissades_per_arr_id(arr_id):
    all_glissades = []
    glissades = find_all_glissades_by_arr_id(arr_id)
    if glissades is None:
        return None
    for glissade in glissades:
        all_glissades.append(glissade.asDictionary())
    return all_glissades

