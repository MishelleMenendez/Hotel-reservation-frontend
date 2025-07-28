from flask import Flask
from flask_restx import Api
from config import Config
from models import db, init_app
from controllers import all_namespaces

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa SQLAlchemy
    init_app(app)

    # Crea la API con documentación Swagger
    api = Api(
        app,
        version="1.0",
        title="Hotel Reservation API",
        description="API para sistema de reservas hoteleras",
        doc="/swagger/"
    )

    # Registra todos los namespaces
    for ns in all_namespaces:
        api.add_namespace(ns)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)