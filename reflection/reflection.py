from mongoengine import connect, StringField, Document, EmbeddedDocument, ReferenceField, ListField, \
    EmbeddedDocumentField


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


# Class_t = type('Test', (Document,), {'num': 0, 'foo': str})
Class_t = type('Test2', (Document,),
               {'num': 0,
                'meta': {'allow_inheritance': True},
                'title': StringField(max_length=120, required=True),
                'tags': ListField(StringField(max_length=30)),
                'comments': ListField(EmbeddedDocumentField(Comment))
                })

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)

# print(type(t1))


# Class_t.dict['bar'] = int
# setattr(Class_t, 'title', StringField(max_length=120, required=True))
# setattr(Class_t, 'author', StringField(max_length=120, required=True))
# setattr(Class_t, 'meta', {'allow_inheritance': True})
# setattr(Class_t, 'tags', ListField(StringField(max_length=30)))
# setattr(Class_t, 'comments', ListField(EmbeddedDocumentField(Comment)))

# t1 = Class_t()

# class TextPost(Class_t):
#    content = StringField()


post1 = Class_t()
post1.title = 'Fun with MongoEngine222222'
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
comment_1 = Comment(name='name', content='content')
comment_2 = Comment(name='name', content='content')
post1.comments = [comment_1, comment_2]
post1.save()

# t1.foo = '1'
# t1.bar = 2
#
# print(t1.foo)
# print(t1.bar)
