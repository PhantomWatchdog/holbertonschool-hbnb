from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from Model.User import User
from Persistence.DataManager import DataManager
import uuid

app = Flask(__name__)
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

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_response_model)
    def get(self):
        '''List all users'''
        print(f"Storage contents: {data_manager.storage}")
        users = data_manager.storage[User].values()
        return list(users)

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_response_model, code=201)
    def post(self):
        '''Create a new user'''
        data = request.json
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if not email or not first_name or not last_name:
            api.abort(400, "Email, first name, and last name are required.")

        # Check if email already exists
        for user in data_manager.storage[User].values():
            if user.email == email:
                api.abort(409, "Email already exists.")

        user = User(email=email, first_name=first_name, last_name=last_name, password="default_password")
        data_manager.save(user)
        print(f"User created: {user.user_id}")
        print(f"Updated storage: {data_manager.storage}")
        return user, 201

@ns.route('/<uuid:user_id>')
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_response_model)
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        print(f"Getting user with id: {user_id}")
        user = data_manager.get(str(user_id), User)  # Ensure user_id is a string
        if user is None:
            print(f"User not found: {user_id}")
            api.abort(404)
        return user

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        print(f"Deleting user with id: {user_id}")
        user = data_manager.get(str(user_id), User)  # Ensure user_id is a string
        if user is None:
            print(f"User not found: {user_id}")
            api.abort(404)
        data_manager.delete(str(user_id), User)
        return '', 204

    @ns.doc('update_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_response_model)
    def put(self, user_id):
        '''Update a user given its identifier'''
        print(f"Updating user with id: {user_id}")
        user = data_manager.get(str(user_id), User)  # Ensure user_id is a string
        if user is None:
            print(f"User not found: {user_id}")
            api.abort(404)

        data = request.json
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)

        data_manager.update(user)
        return user

if __name__ == '__main__':
    app.run(debug=True)
