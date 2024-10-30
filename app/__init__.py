from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# login = LoginManager(app)
# login.login_view = "login"

from app import routes