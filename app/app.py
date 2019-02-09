from flask import Flask

from app.settings import DevConfig

def create_app(config_object=DevConfig):
    app = Flask(__name__)

    from app.main import bp as main_bp
    app.config.from_object(config_object)
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


