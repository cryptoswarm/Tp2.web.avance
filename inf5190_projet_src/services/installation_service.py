from inf5190_projet_src.services.aquatique_inst_services import get_all_aqua_installation_by_arr_id
from inf5190_projet_src.services.arron_service import get_arr_by_name
from inf5190_projet_src.services.glissade_services import get_glissades_per_arr_id
from inf5190_projet_src.services.patinoire_service import get_all_patinoires_by_arr_id





def get_installations_by_arr_name(arr_name):
    all_inst = {}
    arrondissement= get_arr_by_name(arr_name)
    if arrondissement is None:
        return None
    all_inst['arr_name'] = arrondissement.name
    all_inst['arr_cle'] = arrondissement.cle
    aqua_installations, status = get_all_aqua_installation_by_arr_id(arrondissement.id)
    if status == 200:
        all_inst['aqua_inst'] = aqua_installations
    glissades = get_glissades_per_arr_id(arrondissement.id)
    all_inst['glissades'] = glissades
    patinoires =  get_all_patinoires_by_arr_id(arrondissement.id)
    all_inst['patinoires'] = patinoires
    return all_inst
    