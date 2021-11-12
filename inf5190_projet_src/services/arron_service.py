from inf5190_projet_src.repositories.arrondissement_repo import *


def get_arr_by_name(arr_name):
    arrondissement = find_by_arr_name(arr_name)
    if arrondissement is None:
        return {}, 404
    return arrondissement.asDictionary(), 200
