from .flaskr import app, get_db

def create_app():
<<<<<<< HEAD
    
    from . import auth
    from . import blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
=======
    from . import auth
    app.register_blueprint(auth.bp)
>>>>>>> 07b5fb7be97fe0f224108ff48c55c86e1f9f93cc
    return app


create_app()