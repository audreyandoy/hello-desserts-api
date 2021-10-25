from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# new new, bring up during optional session
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/test_desserts_development'
    
    # new new, bring up during optional session
    app.config['SQLALCHEMY_ECHO'] = True

    # Import models here
    

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app


def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    return app
