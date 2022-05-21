from mongoengine import connect
from structure import Structure, StringField, Document

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)

# 实体类的结构
# todo 校验是否存在
structure_server = Structure.objects(name='host')[0]

class_dict = {'num': 0, 'meta': {'allow_inheritance': True}, 'instance_type': StringField()}
for attribute in structure_server.attributes:
    class_dict[attribute.attr_name] = StringField()

# 实体类
InstanceClass = type(structure_server.name, (Document,), class_dict)

i1 = InstanceClass()
i1.instance_type = 'host'  # todo 自动写入初始值
i1.hostname = 'app-server-1'
i1.os = 'centos'
i1.os_version = '7.9'
i1.ip = '10.10.20.1'

# i1.save()

# class SubInstanceClass(InstanceClass):
#     ssh_port = StringField()

# sub_class_dict = InstanceClass.__dict__
# sub_class_dict['ssh_port'] = StringField()

SubInstanceClass = type('linux-host', (InstanceClass,), {'ssh_port': StringField()})

i2 = SubInstanceClass()
i2.instance_type = 'host'
i2.hostname = 'app-server-1'
i2.os = 'centos'
i2.os_version = '7.9'
i2.ip = '10.10.20.2'
i2.ssh_port = '22'

# i2.save()
