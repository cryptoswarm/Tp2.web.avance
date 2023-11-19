from inf5190_projet_src.repositories.coordiantes_repo import *


def get_position_by_hash(hash):
    position = find_by_hash(hash)
    return None if position is None else position


def construct_aqua_position(data):
    pt_x = data[7]
    pt_y = data[8]
    longitude = data[10]
    latitude = data[11]
    position = Coordinate(pt_x, pt_y, longitude, latitude)
    return position


def add_installation_pos(position):
    coordinate = create_inst_aquatique_position(position)
    return coordinate


def get_position_by_id(position_id):
    position = find_by_id(position_id)
    return None if position is None else position
