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


def find_aqua_insta_by_hash(hash):
    return InstallationAquatique.query.filter_by(aqua_hash=hash).first()

def find_aqua_by_id(id):
    return InstallationAquatique.query.filter_by(id=id).first()

def update_aqua(installation, data):
    installation.nom_installation = data['nom_installation']
    installation.type_installation = data['type_installation']
    installation.adress = data['adress']
    installation.propriete_installation = data['propriete_installation']
    installation.gestion_inst = data['gestion_inst']
    installation.equipement_inst = data['equipement_inst']
    

def find_aqua_inst_names_arr_id(arr_id):
    return InstallationAquatique \
           .query \
           .with_entities(InstallationAquatique.nom_installation, InstallationAquatique.id) \
           .filter_by(arron_id=arr_id).all()

def find_aqua_installations(arr_id, aqua_name):
    print('Aqua Repo --> Arrndissement id :{} and aqua_name : {}'.format(arr_id, aqua_name))
    return InstallationAquatique \
           .query \
           .filter(and_(
               (InstallationAquatique.arron_id==arr_id), 
               (InstallationAquatique.nom_installation==aqua_name)
               )).all()
        #    .filter(and_(InstallationAquatique.c.arron_id == arr_id,
        #                    InstallationAquatique.c.nom_installation == aqua_name)).all()
          

# nom_installation = db.Column(db.String(255),  nullable=False)
#     type_installation = db.Column(db.String(255), nullable=False)
#     adress = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
#     propriete_installation = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
#     gestion_inst = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
#     equipement_inst = db.Column(db.String(255),  nullable=False, default='UNKNOWN')
#     aqua_hash = db.Column(db.String(255), unique=True, nullable=False)
#     arron_id = db.Column(db.Integer, ForeignKey('arrondissement.id'))
#     position_id = db.Column(db.Integer, ForeignKey('coordiantes.id'))


