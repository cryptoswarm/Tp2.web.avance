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

 
def save_all_glissade(glissade_as_xml, key_root, key_element, *kwargs):
    content = []
    arr_id = None
    root = xmltodict.parse(glissade_as_xml.text)
    for element in root[key_root][key_element]:
        arr_details = element[kwargs[0][1]]
        details = get_arrondissement_detail(arr_details)
        if find_by_arr_name(details['nom_arr']) is None:
            arrondissement = save_arrondissement(details)
            arr_id = arrondissement.id
        glissade_details = get_glissade_details(element, kwargs)
        glissade_details['date_maj'] = details['date_maj']
        glissade_details['arrondissement_id'] = arr_id
        if find_glissade_by_name(glissade_details['name']) is None:
            save_glissade(glissade_details)
        content.append(details)
    return content


def save_pat_and_conditions(patinoire_as_xml):
    content = []
    count = 0
    arr_id = None
    pat_id = None
    
    root_node = ET.fromstring(patinoire_as_xml.text) # root_node.tag ---> will print [MAIN]
    for child in root_node: #child.tag #<---- list of all arrondissements
        nom_arr = child.find('nom_arr').text.strip()
        content.append(nom_arr)
        if find_by_arr_name(nom_arr) is None:
            new_arr = save_arrondissement({'nom_arr': nom_arr, 'cle': None})
            arr_id = new_arr.id
            content.append(new_arr.asDictionary())
        patinoire = child.find('patinoire')
        for children in patinoire:
            if children.tag == 'nom_pat':
                pat_obj = Patinoire(None, None)
                nom_pat = children.text.strip()
                content.append('children.tag {} and text is {}'.format(children.tag, nom_pat))
                if find_patinoire_by_name(nom_pat) is None:
                    arr_id = find_by_arr_name(nom_arr).id
                    pat_obj.arron_id = arr_id
                    pat_obj.nom_pat = nom_pat
                    new_pat = save_patinoire(pat_obj)
                    pat_id = new_pat.id
                    content.append(new_pat.asDictionary())
            if children.tag == 'condition':
                pat_cond = PatinoirCondition(None, None, None, None, None, None)
                date_heure = datetime.strptime(children.find('date_heure').text.strip(), "%Y-%m-%d %H:%M:%S")
                ouvert = True if children.find('ouvert').text.strip() == '1' else False 
                deblaye = True if children.find('deblaye').text.strip() == '1' else False #children.find('deblaye')
                arrose = True if children.find('arrose').text.strip() == '1' else False #children.find('arrose')
                resurface = True if children.find('resurface').text.strip() == '1' else False #children.find('resurface')
                pat_cond.date_heure = date_heure
                pat_cond.ouvert = ouvert
                pat_cond.deblaye = deblaye
                pat_cond.arrose = arrose
                pat_cond.resurface = resurface
                pat_id =  find_patinoire_by_name(nom_pat).id
                pat_cond.patinoire_id = pat_id
                saved_condition = save_pat_condition(pat_cond)
                content.append(saved_condition.asDictionary())
        #     count += 1
        #     if count == 25:
        #         break
        # break
    return content


