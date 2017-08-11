"""
Users API:

Author: Handerson Contreras.
"""

from flask import request, jsonify
from flask_restful import Resource
from app import API, DB
from models.user import User
from schemas.user import UserSchema
from api.reqparser.user import add_user_parsers


class UsersResource(Resource):
    """Users API."""

    def __init__(self):
        add_user_parsers(self)

    def get(self, user_id):
        user = DB.session.query(User).get(user_id)
        return {'email': user.email}

    def put(self, user_id):
        arguments = self.reqparser.parse_args()
        obj_user = DB.session.query(User).get(user_id)
        obj_user.email = arguments.get('email')

        DB.session.add(obj_user)
        DB.session.commit()

        return 'Updated', 200

class UsersListResource(Resource):
    """Users API."""

    def __init__(self):
        add_user_parsers(self)

    def get(self):
        """Return all Users."""

        return [{'email': user.email} for user in DB.session.query(User).all()]

    def post(self):
        """Create a User."""
        user_schema = UserSchema()
        json_input = request.json
        obj_user, errors = user_schema.load(json_input)

        if errors:
            return jsonify({'errors': errors}), 422
        try:
            DB.session.add(obj_user)
            DB.session.commit()
            return 'saved', 200
        except Exception, e:
            return 'Something went wrong %s' % e, 500

API.add_resource(UsersResource, '/api/v1/users/<user_id>')
API.add_resource(UsersListResource, '/api/v1/users')
