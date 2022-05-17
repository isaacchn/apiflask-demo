from apiflask import APIFlask, Schema
from flask_sqlalchemy import SQLAlchemy
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import os

app = APIFlask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'foo.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                  'mysql://yangxu:root123@10.10.30.32:3306/flask_demo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# class ModelDo(Schema):
#     name = String(required=True, validate=Length(0, 10))


class Model(db.Model):
    __tablename__ = 't_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)


class ModelSchema(Schema):
    name = String(required=True, validate=Length(0, 20))


@app.post('/models')
@app.input(ModelSchema(partial=False))
def create_model(data):
    model = Model()
    model.name = data['name']
    db.session.add(model)
    db.session.commit()


if __name__ == '__main__':
    app.run()
