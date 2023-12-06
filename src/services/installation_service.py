from src.models.installation import Installation
from src.services.aquatique_inst_services import get_aqua_inst_names_arr_id
from src.services.arron_service import get_arr_by_name
from src.services.glissade_services import (
    get_glissades_by_year,
    get_glissades_names_arr_id,
)
from src.services.patinoire_service import (
    get_patinoire_names_arr_id,
    get_patinoires_by_year,
)


def get_inst_names_by_arr_name(arr_name):
    all_inst_names = {}
    arrondissement = get_arr_by_name(arr_name)
    if arrondissement is None:
        return None
    all_inst_names["id"] = arrondissement.id
    all_inst_names["arr_name"] = arrondissement.name
    all_inst_names["arr_cle"] = arrondissement.cle
    aqua_installations = get_aqua_inst_names_arr_id(arrondissement.id)
    if aqua_installations is not None:
        all_inst_names["aqua_inst"] = aqua_installations
    glissades = get_glissades_names_arr_id(arrondissement.id)
    all_inst_names["glissades"] = glissades
    patinoires = get_patinoire_names_arr_id(arrondissement.id)
    all_inst_names["patinoires"] = patinoires
    return all_inst_names


def get_inst_by_year(year):
    glissades = get_glissades_by_year(year)
    patinoires = get_patinoires_by_year(year)
    installations = Installation(glissades, patinoires)
    return installations
