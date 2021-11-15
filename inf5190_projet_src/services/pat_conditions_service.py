from inf5190_projet_src.repositories.pat_condition_repo import find_pat_conditions_by_pat_id


def get_pat_conditions_by_pat_id(pat_id):
    all_conditions = []
    conditions = find_pat_conditions_by_pat_id(pat_id)
    if conditions is None:
        return None
    for condition in conditions:
        all_conditions.append(condition.asDictionary())
    return all_conditions
