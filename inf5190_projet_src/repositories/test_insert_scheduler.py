from inf5190_projet_src import db

def add(instance):
    db.session.add(instance)
    db.session.commit()
    return instance