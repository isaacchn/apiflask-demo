from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

app = APIFlask(__name__)  # 可以使用 title 和 version 参数来自定义 API 的名称和版本
pets = [
    {
        'id': 0,
        'name': 'Kitty',
        'category': 'cat'
    },
    {
        'id': 1,
        'name': 'Coco',
        'category': 'dog'
    }
]


# 定义一个请求数据模式类
class PetInSchema(Schema):
    name = String(required=True, validate=Length(0, 10))  # 可以使用 description 参数添加字段描述
    category = String(required=True, validate=OneOf(['dog', 'cat']))


# 定义一个响应数据模式类
class PetOutSchema(Schema):
    id = Integer()
    name = String()
    category = String()


@app.get('/pets/<int:pet_id>')
@app.output(PetOutSchema)  # 使用 @app.output 装饰器标记响应数据模式
def get_pet(pet_id):
    if pet_id > len(pets) - 1:
        abort(404)
    # 在真实程序里，你可以直接返回 ORM 模型类的实例，比如
    # return Pet.query.get(1)
    return pets[pet_id]


@app.patch('/pets/<int:pet_id>')
@app.input(PetInSchema(partial=True))  # 使用 @app.input 装饰器标记请求数据模式
@app.output(PetOutSchema)
def update_pet(pet_id, data):  # 通过验证后的请求数据字典会注入到视图函数
    if pet_id > len(pets) - 1:
        abort(404)
    for attr, value in data.items():
        pets[pet_id][attr] = value
    return pets[pet_id]


if __name__ == '__main__':
    app.run()
