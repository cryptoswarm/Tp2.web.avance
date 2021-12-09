from inf5190_projet_src import db
from inf5190_projet_src.models.coordiante import Coordinate


def create_inst_aquatique_position(coordiante):
    db.session.add(coordiante)
    db.session.commit()
    return coordiante


def find_by_hash(hash):
    """Testing existence of position by hash, avoid duplication"""
    return Coordinate.query.filter_by(position_hash=hash).first()


def find_by_id(pos_id):
    return Coordinate.query.filter_by(id=pos_id).first()
