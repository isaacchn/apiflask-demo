from mongoengine import connect
from structure import Structure, StringField, Document

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)

# structure_server = Structure.objects(name='host')
structure_server = Structure.objects(name='host')[0]

class_dict = {'num': 0, 'meta': {'allow_inheritance': True}, 'name': StringField()}
for attribute in structure_server.attributes:
    class_dict[attribute.attr_name] = StringField()

InstanceClass = type('Instance', (Document,), class_dict)

i1 = InstanceClass()
i1.name = 'app-server-1'
i1.hostname = 'app-server-1'
i1.os = 'centos'
i1.os_version = '7.9'
i1.ip = '10.10.20.1'

i1.save()
