from mongoengine import connect
from structure import Structure, StringField, Document

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)


def create_class_from_name(name):
    struct = Structure.objects(name=name)[0]
    class_dict = {'num': 0, 'meta': {'allow_inheritance': True}, 'instance_type': name}
    for attribute in struct.attributes:
        class_dict[attribute.attr_name] = StringField()
    return type(name, (Document,), class_dict)


def create_sub_class_from_name(parent_class, name):
    struct = Structure.objects(name=name)[0]
    class_dict = {}
    for attribute in struct.attributes:
        class_dict[attribute.attr_name] = StringField()
    return type(name, (parent_class,), class_dict)


HostClass = create_class_from_name('host')
LinuxHostClass=create_sub_class_from_name(HostClass,'linux_host')

i1 = HostClass()
i1.instance_type = 'host'  # todo 自动写入初始值
i1.hostname = 'app-server-1'
i1.os = 'centos'
i1.os_version = '7.9'
i1.ip = '10.10.20.1'

i1.save()

i2 = LinuxHostClass()
i2.instance_type = 'host'
i2.hostname = 'app-server-1'
i2.os = 'centos'
i2.os_version = '7.9'
i2.ip = '10.10.20.2'
i2.ssh_port = '22'

i2.save()

# 实体类的结构
# todo 校验是否存在
host_struct = Structure.objects(name='host')[0]

class_dict = {'num': 0, 'meta': {'allow_inheritance': True}, 'instance_type': StringField()}
for attribute in host_struct.attributes:
    class_dict[attribute.attr_name] = StringField()

# 实体类
InstanceClass = type(host_struct.name, (Document,), class_dict)

i1 = InstanceClass()
i1.instance_type = 'host'  # todo 自动写入初始值
i1.hostname = 'app-server-1'
i1.os = 'centos'
i1.os_version = '7.9'
i1.ip = '10.10.20.1'

i1.save()

SubInstanceClass = type('linux-host', (InstanceClass,), {'ssh_port': StringField()})

i2 = SubInstanceClass()
i2.instance_type = 'host'
i2.hostname = 'app-server-1'
i2.os = 'centos'
i2.os_version = '7.9'
i2.ip = '10.10.20.2'
i2.ssh_port = '22'

i2.save()
