from flask import Flask
from app.routes.pet_api import pet_route


from app.models.database import engine, Base

def create_app() -> Flask:
    """
    Create flask app instance
    
    """

    flask_app = Flask(__name__)

    Base.metadata.create_all(bind=engine)

    flask_app.register_blueprint(pet_route)


    """
    Register all other things like s3, mail etc
    """
    return flask_app


