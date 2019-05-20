from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True, help = 'Username field cannot be empty.')
    parser.add_argument('password', type=str, required=True, help='Password field cannot be empty.')

    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'The username already exists.'}, 400

        user = UserModel(**data)

        user.save_to_db()

        return {'message': 'User created successfully.'}, 201

class UserList(Resource):
    def get(self):
        return {'users': [x.json() for x in UserModel.query.all()]}