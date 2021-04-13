from flask import Flask, Blueprint, request
from api.blueprint import apiv1

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'This_String_Is_Hard_To_Guess'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
