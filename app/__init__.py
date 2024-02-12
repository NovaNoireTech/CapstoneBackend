from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api= Api(app)
CORS(app)

db= SQLAlchemy(app)
migrate= Migrate(app, db)
jwt= JWTManager(app)

from models.user_model import UserModel
from models import MembershipModel, UserModel

from resources.user import bp as user_bp
api.register_blueprint(user_bp)

from resources.membership import bp as membership_bp
api.register_blueprint(membership_bp)