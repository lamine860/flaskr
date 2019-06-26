from .flaskr import app, get_db

def create_app():
    from . import auth
    app.register_blueprint(auth.bp)
    return app


create_app()