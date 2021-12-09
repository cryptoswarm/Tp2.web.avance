import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config_by_name
from flask_migrate import Migrate
from flask_mail import Mail
from jsonschema import ValidationError


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name):
    # Here the WSGI app object is defined
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5000",
                                             "http://localhost:4200",
                                             "http://10.0.2.15:5000/",
                                             "http://172.28.128.8:5000/",
                                             "https://data-swarm.herokuapp.com"
                                             ]
                                 }
                         },
         expose_headers=["Content-Type", "X-CSRFToken",
                         "Access-Control-Expose-Headers",
                         "USER_ID"],
         supports_credentials=True,
         )
    with app.app_context():
        """App Configurations"""
        app.config.from_object(config_by_name[config_name])

        # db object which is imported by modules and controllers
        db.init_app(app)
        mail.init_app(app)
        migrate.init_app(app, db)

        # HTTP error handling
        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

        # @app.errorhandler(JsonValidationError)
        @app.errorhandler(ValidationError)
        def validation_error(e):
            return jsonify({'error': e.message})

        # using all blueprints
        from inf5190_projet_src.controllers.home_controllers import \
            mod_home as home_module
        # from inf5190_projet_src.controllers.data_requester import \
        #     mod_scheduler as scheduler_mod
        from inf5190_projet_src.controllers.installations_controllers import \
            mod_arron as arrondissement_mod
        from inf5190_projet_src.controllers.glissade_controllers import \
            mod_glissade as glissade_module
        from inf5190_projet_src.controllers.inst_aqua_controllers import \
            insta_aqua as aqua_inst_module
        from inf5190_projet_src.controllers.patinoire_controllers import \
            patinoire as pat_module
        from inf5190_projet_src.controllers.account_controllers import \
            mod_user as user_module

        # Register blueprints
        app.register_blueprint(home_module)
        # app.register_blueprint(scheduler_mod)
        app.register_blueprint(arrondissement_mod)
        app.register_blueprint(glissade_module)
        app.register_blueprint(aqua_inst_module)
        app.register_blueprint(pat_module)
        app.register_blueprint(user_module)

        # Build the database: will create the db file using SQLAlchemy
        # Can be used if we do not want to set migrations
        # db.create_all()

        # configure logger
        if not app.debug and not app.testing:
            '''LOG_TO_STDOUT=1 as env var for heroku'''
            if app.config['LOG_TO_STDOUT']:
                handler = logging.StreamHandler()
                handler.setLevel(logging.INFO)
                app.logger.addHandler(handler)
            else:
                if not os.path.exists('logs'):
                    os.mkdir('logs')
                file_handler = RotatingFileHandler('logs/data_swarm.log',
                                                   maxBytes=10240,
                                                   backupCount=10)
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s %(levelname)s: %(message)s '
                    '[in %(pathname)s:%(lineno)d]'))
                file_handler.setLevel(logging.INFO)
                app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('data swarm start')
    return app
