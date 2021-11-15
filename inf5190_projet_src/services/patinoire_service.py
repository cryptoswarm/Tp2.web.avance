


import re
from inf5190_projet_src.repositories.patinoire_repo import find_patinoires_by_arr_id
from inf5190_projet_src.services.glissade_services import get_patinoire_condition
from inf5190_projet_src.services.pat_conditions_service import get_pat_conditions_by_pat_id


def get_all_patinoires_by_arr_id(arr_id):
    all_patinoires = []
    patinoires = find_patinoires_by_arr_id(arr_id)
    if patinoires is None:
        return None
    for patinoir in patinoires:
        pat = patinoir.asDictionary()
        conditions = get_pat_conditions_by_pat_id(patinoir.id)
        pat['conditions'] = conditions
        all_patinoires.append(pat)
    return all_patinoires