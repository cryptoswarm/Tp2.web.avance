from inf5190_projet_src.repositories.pat_condition_repo import *


def get_pat_conditions_by_pat_id(pat_id):
    all_conditions = []
    conditions = find_pat_conditions_by_pat_id(pat_id)
    if conditions is None:
        return None
    return conditions

def get_pat_condition_cond_id(condition_id):
    condition = find_pat_condition_cond_id(condition_id)
    if condition is None:
        return None, 404
    return condition, 200

def update_pat_condition(existed_cond, new_data):
    updated_cond = update_patinoire_condition(existed_cond, new_data)
    return updated_cond

def delete_pat_condition(condition_id):
    deleted_cond = delete_condition(condition_id)
    return deleted_cond

