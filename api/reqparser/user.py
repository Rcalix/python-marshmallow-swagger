from flask_restful import reqparse

def add_user_parsers(self):
    self.reqparser = reqparse.RequestParser()

    self.reqparser.add_argument(
        'username', dest='username',
        location=('json', 'values'), required=True,
        help='The username',
    )
    self.reqparser.add_argument(
        'email', dest='email',
        location=('json', 'values'), required=True,
        help='The user email',
    )