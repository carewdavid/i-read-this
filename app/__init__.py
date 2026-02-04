import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "articles.db")
    )
    os.makedirs(app.instance_path, exist_ok=True)
    from . import db
    db.init_app(app)
    from . import routes
    app.register_blueprint(routes.bp)
    return app
