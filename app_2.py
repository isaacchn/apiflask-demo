import os

from apiflask import APIFlask, Schema
from flask_sqlalchemy import SQLAlchemy
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# from dto import ModelInSchema, ModelOutSchema

app = APIFlask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'foo.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                  'mysql+pymysql://yangxu:root123@10.10.30.32:3306/flask_demo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# engine = create_engine('mysql+pymysql://yangxu:root123@10.10.30.32:3306/flask_demo')
# session = sessionmaker(bind=engine)
# my_session = session()
#
# Base = declarative_base()
#
#
# class Model(Base):
#     __tablename__ = 't_model'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     data = Column(String)
#
#
# @app.post('/models')
# @app.input(ModelInSchema(partial=False))
# @app.output(ModelOutSchema)
# def create_model(data):
#     model = Model()
#     model.name = data['name']
#     model.data = '{}'
#     my_session.add(model)
#     my_session.commit()
#     out = ModelOutSchema()
#     out['id'] = model.id
#     return ModelOutSchema(id=model.id, name=model.name)


db = SQLAlchemy(app)


class PetModel(db.Model):
    __tablename__ = 't_pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    category = db.Column(db.String(10))


# 资源
class ResourceModel(db.Model):
    __tablename__ = 't_resource'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))


# 资源字段
class ResourceFieldModel(db.Model):
    __tablename__ = 't_resource_field'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))
    resource_id = db.Column(db.Integer, db.ForeignKey('t_resource.id', onupdate=True))


# 资源对象
class ResourceObjModel(db.Model):
    __tablename__ = 't_resource_obj'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    resource_id = db.Column(db.Integer, db.ForeignKey('t_resource.id', onupdate=True))


# 资源字段值
class ResourceValueModel(db.Model):
    __tablename__ = 't_resource_value'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obj_id = db.Column(db.Integer, db.ForeignKey('t_resource_obj.id', onupdate=True))
    field_id = db.Column(db.Integer, db.ForeignKey('t_resource_field.id', onupdate=True))
    value = db.Column(db.String(255))


@app.before_first_request
def init_db():
    db.drop_all()
    db.create_all()
    pets = [
        {'name': 'Kitty', 'category': 'cat'},
        {'name': 'Coco', 'category': 'dog'},
        {'name': 'Flash', 'category': 'cat'}
    ]

    resources = [
        {'id': 1, 'name': 'server'},
        {'id': 2, 'name': 'mysql'}
    ]

    resource_objs = [
        {'id': 1, 'name': 'app-server-01', 'resource_id': 1},
        {'id': 2, 'name': 'app-server-02', 'resource_id': 1},
        {'id': 3, 'name': 'app-server-03', 'resource_id': 1}
    ]

    resource_fields = [
        {'id': 1, 'name': 'os', 'resource_id': 1},
        {'id': 2, 'name': 'ip', 'resource_id': 1},
        {'id': 3, 'name': 'name', 'resource_id': 1},
        {'id': 4, 'name': 'version', 'resource_id': 2},
        {'id': 5, 'name': 'ip', 'resource_id': 2},
        {'id': 6, 'name': 'name', 'resource_id': 2}
    ]

    resource_values = [
        {'field_id': 1, 'value': 'linux'},
    ]
    for pet_data in pets:
        pet = PetModel(**pet_data)
        db.session.add(pet)
    db.session.commit()


class PetInSchema(Schema):
    name = String(required=True, validate=Length(0, 10))
    category = String(required=True, validate=OneOf(['dog', 'cat']))


class PetOutSchema(Schema):
    id = Integer()
    name = String()
    category = String()


@app.get('/')
def say_hello():
    return {'message': 'Hello!'}


@app.get('/pets/<int:pet_id>')
@app.output(PetOutSchema)
def get_pet(pet_id):
    return PetModel.query.get_or_404(pet_id)


@app.get('/pets')
@app.output(PetOutSchema(many=True))
def get_pets():
    return PetModel.query.all()


@app.post('/pets')
@app.input(PetInSchema)
@app.output(PetOutSchema, 201)
def create_pet(data):
    pet = PetModel(**data)
    db.session.add(pet)
    db.session.commit()
    return pet


if __name__ == '__main__':
    app.run()
