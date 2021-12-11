## **Important**:
* Le frontend est fait en utilisant Angular
* Le build est fait en pointant tous les services vers l'adresse de l'api qui est : `http://172.28.128.8:5000`
* S.V.P, utilisez mon `Vagrantfile`, j'ai configuré l'adress ip du `vagrant box`
* Sous `Vagrant`, assurez-vous de lancer le serveur dans l'environnement virtuel avec:
    *  `flask run --host=172.28.128.8 --port=5000`
## Etapes importantes à suivre:

* **Etape1**:  Assurez-vous que la `create_app` du fichier `app.py` prend `"dev"` comme parametre 
* Si vous ne voulez pas configué la `migrations`, :
    * Decommentez la ligne `83` `# db.create_all()` du fichier `__init__.py` du dossier `inf5190_projet_src`
    * Supprimez le dossier `migrations`
    * Sautez à l'etape **Etape4**
* **Etape2**: 
    **Important**
    * Le projet utilise la librairie`Flask-Migrate` qui est un wrapper autour de l'outil de migration `alembic`
    * Vous trouverez un dossier `migrations` dans la racine de projet
    * Executez `flask db upgrade` pour generer les tables
    * Le script `db.sql` a été generer en executant `flask db upgrade --sql > db/db.sql`

* **Etape3**:
    * En ligne de commande executez:
        * cd db/
        * `sqlite3`
        * `.open app.db`
        * `.tables`
        * Vous allez voire que `9 tables` ont été crées. 
        * alembic_version est la table contenant les numeros de versions
* **Etape4**:
    ### Les variables d'environnement:

    * le fichier `.env` doit etre à la racine et doit absolument avoir les valeurs des variables suivantes:
        * FLASK_APP=app.py
        * SECRET_KEY
        * CSRF_SESSION_KEY
        * APP_ADMIN_USERNAME
            * example: APP_ADMIN_USERNAME = 'admin'
        * APP_ADMIN_PASS
        * APP_ADMIN_ID
        * EMAIL_USER
            * example: EMAIL_USER = 'votre Gmail email'
        * EMAIL_PASSWORD
            * example: EMAIL_USER = 'votre Gmail account password'
* **Etape5**:
    * Lancer l'application : `flask run --host=172.28.128.8 --port=5000`

## Les points développés
### Point A1 15xp
* Dans le module `data_requester.py`, vous trouverez les `3` fonctions responsable de l'importation des données.
* `persist_patinoir_data()` importe, parse, valide et insere les données dans les trois tables suivantes:
    * Arrondissement
    * Patinoire 
    * PatinoirCondition
    * Elle prend au minimum `36` minutes 
* `persist_aqua_data()` interroge:
    * Arrondissement : si l'arrondissement existe ou non
    * Coordinate: les coordonnées de l'installation aquatique
    * InstallationAquatique: si l'inst aqua exist ou non
    * Elle prend presque `2` minutes
* `persist_glissade_data()` interroge:
    * Arrondissement
    * Glissade
    * Elle prend quelques secondes
### Point A2 5xp
* Dans le fichier `app.py`, vous trouverez les `3` fonctions responsable de l'importation des données.
* Chaque fonction est donnée à `add_job()` du `scheduler` pour s'executer à `minuit`
* On executes les `3` fonctions decrites dans le point `A1`
### Point A3 5xp
* En production le serveur est déployé dans un dyno séparé du frontend
* Allez à l'url https://flask-data-swarm.herokuapp.com/ pour voire la liste de tous les services `REST`
* Allez à l'url http://172.28.128.8:5000/doc
### Point A4 10xp
* En utilisant `Postman`:
    * Envoyer une requete `Get` à l'url :  `http://172.28.128.8:5000/api/installations?arrondissement=Rivière-des-Prairies–Pointe-aux-Trembles`
    * Réponses:
        * Status code `200`
        * Body:
        ```
            {
                "aqua_inst": [
                    {
                        "id": 2,
                        "nom_installation": "Saint-Jean-Baptiste"
                    },
                    {
                        "id": 54,
                        "nom_installation": "Centre aquatique Rivières-des-Prairies"
                    }
                ],
                "arr_cle": null,
                "arr_name": "Rivière-des-Prairies–Pointe-aux-Trembles",
                "glissades": [
                    {
                        "id": 1,
                        "name": "Aire de glissade ,Don-Bosco"
                    },
                    {
                        "id": 2,
                        "name": "Aire de glissade,François-Vaillancourt"
                    }
                ],
                "id": 13,
                "patinoires": [
                    {
                        "id": 158,
                        "nom_pat": "Aire de glissade,Saint-Jean-Baptiste ()"
                    },
                    {
                        "id": 159,
                        "nom_pat": "Aire de glissade,Saint-Joseph ()"
                    }
                ]
            }
        ``` 
        * Status code `404`
        * Body:
        ```
        {
            "message": "No installations has been found, check the name of the arrondissement"
        }
        ```
### Point A5 10xp
* Saisir le nom d'un arrondissement
* Si l'arrondissement est existance, 3 onglets vont etre affichés
* chacun pour une categorie d'installation
* Sinon, un message d'erreur va etre affiché
* Example: 
    * Saisir `LaSalle` comme etant le nom de l'arrondissement
    * `Installations Aquatiques`, `Glissades` et `Patinoires` sont les 3 onglets qui vont etre affichés
    * chaque onglet affuche le nom d'installation trouvé
    * chaque onglet est prépublié par les noms d'installations

### Point A6 10xp
* Apres avoir lancé la recherche, il reste à chosir le nom d'installation de la categrie de votre choix. 
* Si aucune installation n'existe pour une categorie donné, l'option de choisir une installation va etre déactivée.
* Il suffit de choisir un nom d'installation
* Toutes les informations de l'installations vont etre affiché
* Pour la categorie `Patinoires`, vous devez selectionner `l'année` apres avoir choisit le nom de la `patinoire`

### Point C1 10xp
* En utilisant `Postman`:
* Envoyer une request `GET` à l'url:
    * http://172.28.128.8:5000/api/installations/2021
    * Vous pouvez choisir la date que vous souhaitez
    * Si vous voulez obtenir un Json, assurez-vous de choisir `application/json` comme `Content-Type` dans les `Headers`
    * Le contenu est compressé en raison que la réponse est volumineuse. au lieu de 56MB la taille final est de l'ordre de 1.70MB
    * Presque 20 secondes sont necissaires avant de recevoir la réponse. 
### Point C2 10xp
* En utilisant `Postman`:
* Envoyer une request `GET` à l'url:
    * http://172.28.128.8:5000/api/installations/2021
    * Vous pouvez choisir la date que vous souhaitez
    * Si vous voulez recevoir un xml, assurez-vous de choisir `application/xml` comme `Content-Type` dans les `Headers`
    * La réponse prend au moins 2 minutes

### Point D1 15xp
* En utilisant `Postman`:
    * Avant tous, vous devez obtenir le id de la glissade de votre choix
    * Soit vous envoyer une request `GET` à l'url: 
        * `http://172.28.128.8:5000/api/installations?arrondissement=Rivière-des-Prairies–Pointe-aux-Trembles`
    * Dans le array `"glissades"` vous trouverez les `id` et le `nom` du glissade 
    * Sinon envoyer une request `GET` à l'url :
        * `http://172.28.128.8:5000/api/installations/arrondissement/<name>/glissade/<name>` 
    * Si les nom d'arrondissement et de la glissade sont corrects vous allez obtenir:
        ```
        {
            "arrondissement_id": 13.0,
            "condition": "N/A",
            "date_maj": "2021-10-18T13:45:13",
            "deblaye": false,
            "id": 5.0,
            "name": "Aire de glissade,Saint-Joseph",
            "ouvert": false
        }
        ```
    * Envoyer une requete `PUT` à l'url :  `http://172.28.128.8:5000/api/glissade/1`
    * Example d'une good request
        * Le payload requis est :
        ```
            {
                "name": "Aire de glissade,Saint-Joseph",
                "date_maj": "2014-08-17T14:58:57.600623+00:00",
                "ouvert": "0",
                "deblaye": "0",
                "condition": "N/A",
                "arrondissement_id": 13
            }
        ```
        * Réponse:
        * Status code : `200`
        * Body:
        ```
        {
            "arrondissement_id": 13.0,
            "condition": "N/A",
            "date_maj": "2014-08-17T14:58:57.600623",
            "deblaye": false,
            "id": 1.0,
            "name": "Aire de glissade ,Don-Bosco",
            "ouvert": false 
        }
        ```
    * Examples d'une bad request
    1. Payload erroné: `Manque des champs requis`
        ```
        {
                "arrondissement_id": 13.0,
                "condition": "N/A",
        }
        ```
        * Status code : `400`
        * Body:
        ```
        {
            "arrondissement_id": [
                "Missing data for required field."
            ],
            "condition": [
                "Missing data for required field."
            ],
            "deblaye": [
                "Missing data for required field."
            ],
            "ouvert": [
                "Missing data for required field."
            ]
        }
        ```
    2. Payload erroné: `Champ requis id de l'arrondissement incorrect`
        ```
        {
            "name": "Aire de glissade,Saint-Joseph",
            "date_maj": "2014-08-17T14:58:57.600623+00:00",
            "ouvert": "0",
            "deblaye": "0",
            "condition": "N/A",
            "arrondissement_id": 198
        }
        ```
        * Status code : `400`
        * Body:
        ```
        {
            "message": "arrondissement does not exist!"
        }
        ```
    3. Payload erroné: `Champ requis date incorrecte`
        ```
        {
            "name": "Aire de glissade,Saint-Joseph",
            "date_maj": "2014-08-17T14",
            "ouvert": "0",
            "deblaye": "0",
            "condition": "N/A",
            "arrondissement_id": 198
        }
        ```
        * Status code : `400`
        * Body:
        ```
        {
            "date_maj": [
                "Not a valid datetime."
            ]
        }
        ```
    4. Payload correcte mais l'id de la glissade est incorrecte
        * Status code : `404`
        * Body:
        ```
        {
            "message": "Glissade does not exist!"
        }
        ```
### Point D2 5xp
* En utilisant `Postman`:
    * Envoyer une requete `Delete` à l'url :  `http://172.28.128.8:5000/api/glissade/<id>` 
    * Vous devez envoyé le `Authorization` header:
        * Dans l'onglet `Authorization` séléctionner `Basic auth` de la liste déroulante `type`
        * Dans le champ `Username`:  Entrer `admin`
        * Dans le champ `Password`:  Entrer `supersecret`
    * Réponses:
        * Status code `200`
        * Body de la glissade supprimé
        ```
        {
            "arrondissement_id": 13.0,
            "condition": "N/A",
            "date_maj": "2014-08-17T14:58:57.600623",
            "deblaye": false,
            "id": 1.0,
            "name": "Aire de glissade ,Don-Bosco",
            "ouvert": false
        }
        ```
        * Status code `404`, il suffit seuelemnt de reexecuter la requete en haut
        * Body:
        ```
        {
            "message": "glissade does not exist",
            "status": "fail"
        }
        ```








### Point E4 20 pts
1. Dans le fichier `.env`, **assurez-vous** d'avoir des valeurs pour les 3 variables suivants:
    * `APP_ADMIN_USERNAME="admin"`
    * `APP_ADMIN_PASS="supersecret"`
    * `APP_ADMIN_ID= "7"`
1. En utilisant `Postman`:
    * Envoyer une requete `Post` à l'url :  `http://172.28.128.8:5000/api/authenticate`
    * Dans l'onglet `Authorization` séléctionner `Basic auth` de la liste déroulante `type`
    * Good request:
        * Dans le champ `Username`:  Entrer `admin`
        * Dans le champ `Password`:  Entrer `supersecret`
        * Réponse:
            * Status code:  `200`
            * Headers: 
             
            | key       | value           | 
            | ------------- |:-------------:|
            | `Set-Cookie`      | session=eyJ1c2VyX2lkIjo0Nzk0NzE0OTg3Mjc4NTc2ODQ2fQ.Ya6Iow.uJRlKbWDyo9nSh6_PuCDeMEIE14; HttpOnly; Path=/; SameSite=Lax |
            * Body : `null`
    * Bad request:
        * Dans le champ `Username`:  Entrer `wrong`
        * Dans le champ `Password`:  Entrer `supersecret`
        * Réponse:
            * Status code:  `401`
            * Headers: 
            * Body
            ```
            {
                "message": "Please authenticate."
            }
            ```

### Point E1 10 pts
* En utilisant `Postman`:
    * Envoyer une requete `Post` à l'url :  `http://172.28.128.8:5000/api/profile` 
    * Dans la requete, on s'attend à avoir un payload tel qu'il montré par l'example suivant:
    ```
    {
        "complete_name": "mokhtar safir",
        "email": "mokhtar@hotmail.fr",
        "followed_arr": [
            "Verdun",
            "LaSalle"
        ]
    }
    ```
    * Réponses:
        * Status code 200 accompagné du payload suivant:
        ```
        {
            "complete_name": "mokhtar safir",
            "email": "mokhtar@hotmail.fr",
            "followed_arr": [
                "{'id': 90, 'name': 'Verdun', 'profile_id': 32}",
                "{'id': 91, 'name': 'LaSalle', 'profile_id': 32}"
            ],
            "id": 32.0
        }
        ```   
        * Status code 400 accompagné du :
        ```
        {
            "message_email": "Email is Already Registered"
        }
        ```
        * Status code 400 accompagné du :
        ```
        {
            "followed_arr_err": "Shorter than minimum length 1."
        }
        ```
        est retourné si `followed_arr` est vide
        * Status code 400 accompagné du :
        ```
        {
            "message_email": [
                "The domain name hotmail.fre does not exist."
            ]
        }
        ```
        est retourné si le domaine de l'email est incorrect: ex: `mokhtar@hotmail.fre`
* En ligne de commande comme:
    * Envoyer:
    ```
        curl --request POST \
        --url "http://172.28.128.8:5000/api/profile" \
        --data '{"complete_name": "mokhtar safir"}' \
        --header 'Content-type:application/json' \
        --include
    ```
    * Réponse:
    ```
        HTTP/1.0 400 BAD REQUEST
        Content-Type: application/json
        Content-Length: 113
        Access-Control-Allow-Origin: http://127.0.0.1:5000
        Access-Control-Expose-Headers: Access-Control-Expose-Headers, Content-Type, USER_ID, X-CSRFToken
        Access-Control-Allow-Credentials: true
        Vary: Origin
        Server: Werkzeug/2.0.1 Python/3.9.1
        Date: Mon, 06 Dec 2021 21:45:23 GMT
        {
            "email_err": "Missing data for required field.", 
            "followed_arr_err": "Missing data for required field."
        }
    ```
### Point F 20 pts:
* En raison que le dyno pourrait etre en mode hybernation, allez à l'url du serveur : https://flask-data-swarm.herokuapp.com/
* Ensuite, l'application qui est deployée sur un autre dyno à l'url : https://data-swarm.herokuapp.com/
* L'application en production utilise `postgres sql` comme db et `angular` pour le frontend

* Remarques: 
    * Le boutton de `suppression` n'apparait que si vous etes authentifié.
    * le boutton de `unsubscribe` n'apparait que si vous avez crée un profil