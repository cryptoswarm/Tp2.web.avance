import logging
import datetime
import pytz
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from flask_json_schema import JsonSchema, JsonValidationError



db = SQLAlchemy()
schema = JsonSchema()

def create_app(test_config=None):
    # Here the WSGI app object is defined
    app = Flask(__name__)
    # CORS(app) or the way below 
    # CORS(app, resources=r'/*', headers='Content-Type') or
    # CORS(app, resources={r"/*": {"origins":"*"}},headers='Content-Type') #or
    #CORS(app, resources={r"/*": {"origins":"http://localhost:4200"}},headers='Content-Type') #or
    # CORS(app, resources={r"/*": {"origins":["http://localhost:4200", "http://localhost:5000"]}},headers='Content-Type')
    # e.g., CORS(app, origins=[“http://localhost:8000”, “https://example.com”]).
    # CORS(app, resources={r"/*": {"origins":"http://localhost:4200"}},headers='Content-Type')
    CORS(app, resources={r"/*": {"origins":["http://127.0.0.1:5000", "http://localhost:4200"]}},headers='Content-Type')
    
    # app.config['CORS_HEADERS'] = "Content-Type"
    # app.config['CORS_RESOURCES'] = {r'/*': {"origins":"*"}}
    # CORS(app)
    #logging.basicConfig()
    #logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

    with app.app_context():
    # Configurations
        
        app.config.from_object('config')

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile("config.py", silent=True)
        else:
            # load the test config if passed in
            app.config.update(test_config)

        # The folowing fct is for test purposes only
        @app.route("/hello")
        def hello():
            return "Hello, World!"

        # db object which is imported by modules and controllers
        db.init_app(app)
        schema.init_app(app)

        # HTTP error handling
        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

        @app.errorhandler(JsonValidationError)
        def validation_error(e):
            return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]}), 400
        

        # Import the only module in the app which is article, 
        # using its blueprint handler var (mod_article)
        from inf5190_projet_src.mod_app.controllers import mod_home as home_module
        from inf5190_projet_src.controllers.data_requester import mod_scheduler as scheduler_mod
        from inf5190_projet_src.controllers.aqua_controllers import mod_arron as arrondissement_mod
        from inf5190_projet_src.controllers.glissade_controllers import mod_glissade as glissade_module
        from inf5190_projet_src.controllers.inst_aqua_controllers import insta_aqua as aqua_inst_module

        # Register blueprints
        app.register_blueprint(home_module)
        app.register_blueprint(scheduler_mod)
        app.register_blueprint(arrondissement_mod)
        app.register_blueprint(glissade_module)
        app.register_blueprint(aqua_inst_module)


        # Build the database: will create the db file using SQLAlchemy
        db.create_all()

        # make url_for('accueil') == url_for('article.accueil')
        # in another app, you might define a separate main accueil here with
        # app.route, while giving the article blueprint a url_prefix, but for
        # the tutorial the article will be the main index
        #app.add_url_rule("/", endpoint="accueil")

    return app

application = create_app()