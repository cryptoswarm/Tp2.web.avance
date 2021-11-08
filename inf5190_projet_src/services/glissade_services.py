import xmltodict
from datetime import datetime
from inf5190_projet_src.repositories.arrondissement_repo import save_arrondissement
from inf5190_projet_src.repositories.glissade_repo import *



#url_patinoire = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"

def get_arrondissement_detail(arr_details):
    nom_arr = arr_details['nom_arr']
    cle = arr_details['cle']
    date_maj = datetime.strptime(arr_details['date_maj'], "%Y-%m-%d %H:%M:%S")
    return {'nom_arr':nom_arr, 'cle':cle, 'date_maj': date_maj}


# def save_arrondissement(content):
#     save_arrondissement(content)


def save_items(glissade_as_xm, key_root, key_element, *kwargs):
    content = []
    root = xmltodict.parse(glissade_as_xm.text)
    for element in root[key_root][key_element]:
        print(kwargs[0][0])
        #content.append(])
        arrondissement = element[kwargs[0][1]]
        details = get_arrondissement_detail(arrondissement)
        save_arrondissement(details)
        #content.append(arrondissement)
        content.append(details)
        #save_arrondissement()
    return content


