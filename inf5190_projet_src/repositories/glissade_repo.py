from inf5190_projet_src import db
from models.glissade import Glissade
from sqlalchemy import or_, and_, func, desc


def save_glissade(content):
    glissade = Glissade(content.name, content.date_maj, 
                              content.ouvert, content.deblaye,
                              content.condition, content.arrondissement_id)
    db.session.add(glissade)
    db.session.commit()
    return glissade