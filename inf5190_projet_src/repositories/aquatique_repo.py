from flask_sqlalchemy import Pagination
from inf5190_projet_src import db
from inf5190_projet_src.models.piscines_aquatique import InstallationAquatique
from sqlalchemy import or_, and_, func, desc



def save_installation_aquatique(aquatique_insta):
    print('Insta aquatique received :',aquatique_insta.asDictionary())
    db.session.add(aquatique_insta)
    db.session.commit()
    print(print('Insta aquatique created :',aquatique_insta.asDictionary()))
    return aquatique_insta

def find_all_aqua_installation_by_arr_id(arr_id):
    return InstallationAquatique.query.filter_by(arron_id=arr_id).all()


