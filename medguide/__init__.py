from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)

    from .views import views
    from .extents import extents

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(extents,url_prefix='/')


    return app






