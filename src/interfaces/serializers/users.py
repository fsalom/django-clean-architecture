from marshmallow import Schema, fields


class UserSerializer(Schema):
    first_name = fields.String(required=True)
    email = fields.String(required=True)
