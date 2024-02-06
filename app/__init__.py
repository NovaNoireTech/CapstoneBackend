from flask import Flask

app = Flask(__name__)

from resources.membership import routes
from resources.user import routes