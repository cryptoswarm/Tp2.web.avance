import xmltodict
from datetime import datetime
from inf5190_projet_src.repositories.arrondissement_repo import *
from inf5190_projet_src.repositories.glissade_repo import *



#url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"

def get_arrondissement_detail(arr_details):
    nom_arr = arr_details['nom_arr']
    cle = arr_details['cle']
    date_maj = datetime.strptime(arr_details['date_maj'], "%Y-%m-%d %H:%M:%S")
    return {'nom_arr':nom_arr, 'cle':cle, 'date_maj': date_maj}



# <glissade>
#         <nom>Aire de glissade ,Don-Bosco</nom>
#         <arrondissement>
#             <nom_arr>RiviÃ¨re-des-Prairies - Pointe-aux-Trembles</nom_arr>
#             <cle>rdp</cle>
#             <date_maj>2021-10-18 13:45:13</date_maj>
#         </arrondissement>
#         <ouvert>0</ouvert>
#         <deblaye>0</deblaye>
#         <condition>N/A</condition>
#     </glissade>

def get_glissade_details(element, kwargs):
    glissade_name = element[kwargs[0][0]]
    print('type of element[kwargs[0][2]] :', type(element[kwargs[0][2]]))
    ouvert = False if element[kwargs[0][2]] == '0' else True
    deblaye = False if element[kwargs[0][3]] == '0' else True
    condition = element[kwargs[0][4]]
    return {'name':glissade_name, 'ouvert':ouvert, 'deblaye':deblaye, 'condition':condition}


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


