from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .views import views

limiter = Limiter(key_func=get_remote_address, default_limits="[20 per day]")

def create_app():
    app = Flask(__name__)
    limiter.init_app(app)
    
    app.register_blueprint(views)
    
    return app