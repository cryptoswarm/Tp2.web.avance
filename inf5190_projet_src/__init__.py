import logging
import pytz
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from config import JOB_STORE_URL

db = SQLAlchemy()

# jobstores = {
#     'default': SQLAlchemyJobStore(JOB_STORE_URL)
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }

# from inf5190_projet_src.controllers.data_requester import save_uploaded_data
# scheduler = BackgroundScheduler(jobstores=jobstores)
# #scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
# scheduler.add_job(func=save_uploaded_data, trigger='interval', minutes=2, timezone=pytz.utc)  #timezone=pytz.utc.dst
# #start the scheduler
# scheduler.start()

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
        #db = SQLAlchemy(app)
        db.init_app(app)

        # HTTP error handling
        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

        

        # Import the only module in the app which is article, 
        # using its blueprint handler var (mod_article)
        from inf5190_projet_src.mod_app.controllers import mod_home as home_module
        from inf5190_projet_src.controllers.data_requester import mod_scheduler as scheduler_mod

        # Register blueprints
        app.register_blueprint(home_module)
        app.register_blueprint(scheduler_mod)


        # Build the database: will create the db file using SQLAlchemy
        db.create_all()

        # make url_for('accueil') == url_for('article.accueil')
        # in another app, you might define a separate main accueil here with
        # app.route, while giving the article blueprint a url_prefix, but for
        # the tutorial the article will be the main index
        #app.add_url_rule("/", endpoint="accueil")
        
        # #Import function that will be executed by the scheduler
        # from inf5190_projet_src.controllers.data_requester import save_uploaded_data
        # scheduler = BackgroundScheduler(jobstores=jobstores)
        # #scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
        # scheduler.add_job(func=save_uploaded_data, trigger='interval', minutes=2, timezone=pytz.utc)  #timezone=pytz.utc.dst
        # #start the scheduler
        # scheduler.start()
        # from inf5190_projet_src.controllers.data_requester import run_job
        # run_job(app)
    return app