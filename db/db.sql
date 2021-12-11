CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 171161f23aa0

CREATE TABLE arrondissement (
    id INTEGER NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    cle VARCHAR(50), 
    PRIMARY KEY (id), 
    UNIQUE (cle), 
    UNIQUE (name)
);

CREATE TABLE coordinates (
    id INTEGER NOT NULL, 
    point_x VARCHAR(255) NOT NULL, 
    point_y VARCHAR(255) NOT NULL, 
    longitude VARCHAR(255) NOT NULL, 
    latitude VARCHAR(255) NOT NULL, 
    position_hash VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (position_hash)
);

CREATE TABLE profile (
    id INTEGER NOT NULL, 
    complete_name VARCHAR(255) NOT NULL, 
    email VARCHAR(80) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (email)
);

CREATE TABLE glissade (
    id INTEGER NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    date_maj DATETIME NOT NULL, 
    ouvert BOOLEAN NOT NULL, 
    deblaye BOOLEAN NOT NULL, 
    condition VARCHAR(255) NOT NULL, 
    arrondissement_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(arrondissement_id) REFERENCES arrondissement (id), 
    UNIQUE (name)
);

CREATE TABLE installation_aquatique (
    id INTEGER NOT NULL, 
    nom_installation VARCHAR(255) NOT NULL, 
    type_installation VARCHAR(255) NOT NULL, 
    adress VARCHAR(255) NOT NULL, 
    propriete_installation VARCHAR(255) NOT NULL, 
    gestion_inst VARCHAR(255) NOT NULL, 
    equipement_inst VARCHAR(255) NOT NULL, 
    aqua_hash VARCHAR(255) NOT NULL, 
    arron_id INTEGER, 
    position_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(arron_id) REFERENCES arrondissement (id), 
    FOREIGN KEY(position_id) REFERENCES coordinates (id), 
    UNIQUE (aqua_hash)
);

CREATE TABLE patinoire (
    id INTEGER NOT NULL, 
    nom_pat VARCHAR(255) NOT NULL, 
    arron_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(arron_id) REFERENCES arrondissement (id), 
    UNIQUE (nom_pat)
);

CREATE TABLE profile_arrondissement (
    id INTEGER NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    profile_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(profile_id) REFERENCES profile (id)
);

CREATE TABLE patinoir_condition (
    id INTEGER NOT NULL, 
    date_heure DATETIME NOT NULL, 
    ouvert BOOLEAN NOT NULL, 
    deblaye BOOLEAN NOT NULL, 
    arrose BOOLEAN NOT NULL, 
    resurface BOOLEAN NOT NULL, 
    patinoire_id INTEGER, 
    pat_hash VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(patinoire_id) REFERENCES patinoire (id), 
    UNIQUE (pat_hash)
);

INSERT INTO alembic_version (version_num) VALUES ('171161f23aa0');

