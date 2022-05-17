from main import CustomAPIFlask
from mongoengine import connect, StringField, Document, EmbeddedDocument, ReferenceField, ListField, \
    EmbeddedDocumentField

app = CustomAPIFlask(__name__)
connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def __repr__(self):
        return self.first_name + ' ' + self.last_name + ' <' + self.email + '>'


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    meta = {'allow_inheritance': True}
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley')
ross.save()

post1 = TextPost(title='Fun with MongoEngine', author=ross)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()

for user in User.objects():
    print(user.email)

# if __name__ == '__main__':
#     app.run()
