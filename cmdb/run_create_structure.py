from structure import Structure, StructureAttribute
from mongoengine import connect, StringField

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)

host = Structure()
host.name = 'host'
host.description = '主机'
host.parent_structure = None
# hostname_attr = Attribute(attr_name='hostname', attr_description='主机名')
# os_attr = Attribute(attr_name='os', attr_description='操作系统')
# os_version_attr = Attribute(attr_name='os_version', attr_description='操作系统版本')
# ip_attr = Attribute(attr_name='ip', attr_description='IP地址')

host.attributes = [
    StructureAttribute(attr_name='hostname', attr_description='主机名'),
    StructureAttribute(attr_name='os', attr_description='操作系统'),
    StructureAttribute(attr_name='os_version', attr_description='操作系统版本'),
    StructureAttribute(attr_name='ip', attr_description='IP地址')
]
host.save()
# Structure.objects(name=host.name).update_one(description=host.description, attributes=host.attributes)

mysql = Structure()
mysql.name = 'mysql'
mysql.description = 'MySQL数据库'
host.parent_structure = None
mysql.attributes = [
    StructureAttribute(attr_name='ip', attr_description='IP地址'),
    StructureAttribute(attr_name='port', attr_description='端口'),
    StructureAttribute(attr_name='x_port', attr_description='x协议端口'),
    StructureAttribute(attr_name='major_version', attr_description='主版本号')
]
mysql.save()
# Structure.objects(name=mysql.name).update_one(description=mysql.description, attributes=mysql.attributes)

linux_host = Structure()
linux_host.name = 'linux_host'
linux_host.description = 'Linux主机'
linux_host.parent_structure = 'host'
linux_host.attributes = [
    StructureAttribute(attr_name='ssh_port', attr_description='SSH端口')
]

linux_host.save()
