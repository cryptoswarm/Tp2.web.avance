
from flask_sqlalchemy import Pagination
from inf5190_projet_src import db
from inf5190_projet_src.models.coordiante import Coordinate
from sqlalchemy import or_, and_, func, desc



def create_inst_aquatique_position(coordiante):
    print('Coordiante aquatique received :',coordiante.asDictionary())
    db.session.add(coordiante)
    db.session.commit()
    print(print('Coordiante created :',coordiante.asDictionary()))
    return coordiante

def find_by_hash(hash):
    print('Testing existence of position by hash :', hash)
    return Coordinate.query.filter_by(position_hash=hash).first()

def find_by_id(pos_id):
    return Coordinate.query.filter_by(id=pos_id).first()

    
