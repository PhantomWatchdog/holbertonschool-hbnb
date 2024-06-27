from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy  # Étape 1: Importer SQLAlchemy
from Model.User import User
from Persistence.DataManager import DataManager
import uuid

app = Flask(__name__)
# Étape 2: Configurer l'application pour utiliser SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Étape 3: Initialiser SQLAlchemy avec l'application Flask

api = Api(app, version='0.1', title='HBnB API Test version')

data_manager = DataManager()

ns = api.namespace('Users Actions')

user_model = api.model('User Attributs', {
    'email': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
})

user_response_model = api.model('User Request Response', {
    'user_id': fields.String,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})

# Le reste de votre code reste inchangé...

if __name__ == '__main__':
    app.run(debug=True)