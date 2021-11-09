from threading import Condition
import xmltodict
from datetime import datetime
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.repositories.glissade_repo import *
from inf5190_projet_src.repositories.patinoire_repo import find_patinoire_by_name, save_patinoire
from inf5190_projet_src.repositories.pat_condition_repo import *

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
 
def save_items(glissade_as_xml, key_root, key_element, *kwargs):
    content = []
    arr_id = None
    root = xmltodict.parse(glissade_as_xml.text)
    for element in root[key_root][key_element]:
        # print(kwargs[0][0]) # nom
        # print(kwargs[0][1]) # arrondissement
        # #content.append(])
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

#'MAIN', 'arrondissement', ['nom_arr', 'patinoire']
def save_pat_and_conditions(patinoire_as_xml, key_root, key_element, *kwargs):
    #write_response_to_file(patinoire_as_xml.text, 'patinoire.xml')
    content = []
    arr_id = None
    pat_id = None
    root = xmltodict.parse(patinoire_as_xml.text)
    for element in root[key_root][key_element]:
        print('kwargs[0][0] :',kwargs[0][0]) #nom_arr
        print('kwargs[0][1]] :',kwargs[0][1]) #patinoire
        nom_arr = element[kwargs[0][0]] # nom_arr
        print('nom_arr :',nom_arr)
        patinoire_details = element[kwargs[0][1]] # patinoire -> name and list of condition
        with open('patinoire.text', 'w') as f:
            f.write(str(patinoire_details))
        #print('pat_details :', pat_details)
        # pat_conditions = get_patinoire_details(element)
        # if find_by_arr_name(nom_arr) is None:
        #     arr_details = {'nom_arr':nom_arr, 'cle':None}
        #     arrondissement = save_arrondissement(arr_details)
        #     arr_id = arrondissement.id

        # nom_pat = pat_conditions['nom_pat']
        # #print('nom_pat = pat_conditions[nom_pat] :',nom_pat)
        # if find_patinoire_by_name(nom_pat) is None:
        #     pat_details = {'nom_pat':nom_pat, 'arron_id':arr_id}
        #     patinoire = save_patinoire(pat_details)
        #     pat_id = patinoire.id

        # for condition in pat_conditions['conditions']:
        #     condition['patinoire_id'] = pat_id
        #     save_pat_condition(condition)
            
        content.append(element)
        break
    return content


