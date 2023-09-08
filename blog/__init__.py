from flask import Flask, render_template
from .config.variables import SECRET_KEY

def create_app():
    app = Flask(__name__)

    # CONFIG
    app.config["SECRET_KEY"] = SECRET_KEY


    # BLUEPRINT
    from .views.admin_auth import admin_auth
    app.register_blueprint(admin_auth, url_prefix="/owner")

    #ERROR ROUTE
    # 404
    @app.errorhandler(404)
    def error_404(error):
        return render_template("error-404.html")
    
    # 500
    @app.errorhandler(Exception)
    def error_500(error):
        return render_template("error-500.html")
    
    # REGISTER
    

    return app