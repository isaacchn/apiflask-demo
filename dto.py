from apiflask import Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length


class ModelInSchema(Schema):
    name = String(required=True, validate=Length(0, 20))


class ModelOutSchema(Schema):
    id = Integer()
    name = String()
