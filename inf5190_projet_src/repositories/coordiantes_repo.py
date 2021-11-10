
from flask_sqlalchemy import Pagination
from inf5190_projet_src import db
from inf5190_projet_src.models.coordiante import Coordiante
from sqlalchemy import or_, and_, func, desc



def save_inst_aquatique_position(coordiante):
    print('Coordiante aquatique received :',coordiante.asDictionary())
    db.session.add(coordiante)
    db.session.commit()
    print(print('Coordiante created :',coordiante.asDictionary()))
    return coordiante