from models.user import User
from app import MA

class UserSchema(MA.ModelSchema):
    class Meta:
        model = User
