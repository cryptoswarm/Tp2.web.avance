from datetime import datetime
from xml.etree.ElementTree import Element
from src.repositories.pat_condition_repo import *


def get_pat_conditions_by_pat_id(pat_id):
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


def add_pat_condition(data: Element, pat_id: int):
    date_heure = datetime.strptime(
        data.find("date_heure").text.strip(), "%Y-%m-%d %H:%M:%S"
    )
    ouvert = True if data.find("ouvert").text.strip() == "1" else False
    deblaye = True if data.find("deblaye").text.strip() == "1" else False
    arrose = True if data.find("arrose").text.strip() == "1" else False
    resurface = True if data.find("resurface").text.strip() == "1" else False
    pat_cond = PatinoirCondition(date_heure, ouvert, deblaye, arrose, resurface, pat_id)
    existed_cond = find_pat_cond_by_hash(pat_cond.pat_hash)
    if existed_cond is None:
        existed_cond = save_pat_condition(pat_cond)
    return existed_cond


def get_pat_cond_by_hash(hash):
    pat_cond = find_pat_cond_by_hash(hash)
    if pat_cond is None:
        return None
    return pat_cond


def get_pat_conditions_by_year(year):
    pat_conditions = find_pat_conditions_by_year(year)
    if len(pat_conditions) == 0:
        return None
    return pat_conditions


def get_pat_ids_from_conditions_by_year(year):
    pat_conditions_ids = find_pat_ids_from_conditions_by_year(year)
    return pat_conditions_ids
