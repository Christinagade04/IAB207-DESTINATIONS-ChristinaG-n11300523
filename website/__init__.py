from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # we use this utility module to display forms quickly
    Bootstrap5(app)

    # A secret key for the session object
    app.secret_key = 'somerandomvalue'

    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///websitedb.sqlite'
    db.init_app(app)

    # config upload folder
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.event_db)
    from . import auth
    app.register_blueprint(auth.authbp)

    return app