from flask import Flask

import settings
from apps.product.view import product_bp
from apps.user.view import user_bp
from exts import db, bootstrap


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)

    db.init_app(app)
    bootstrap.init_app(app)
    return app