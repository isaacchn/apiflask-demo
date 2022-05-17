from structure import Structure, StructureAttribute
from mongoengine import connect, StringField

connect(
    host='mongodb://admin:admin@10.10.30.32/cmdb?authSource=admin'
)

server = Structure()
server.name = 'host'
server.description = '主机'

# hostname_attr = Attribute(attr_name='hostname', attr_description='主机名')
# os_attr = Attribute(attr_name='os', attr_description='操作系统')
# os_version_attr = Attribute(attr_name='os_version', attr_description='操作系统版本')
# ip_attr = Attribute(attr_name='ip', attr_description='IP地址')

server.attributes = [
    StructureAttribute(attr_name='hostname', attr_description='主机名'),
    StructureAttribute(attr_name='os', attr_description='操作系统'),
    StructureAttribute(attr_name='os_version', attr_description='操作系统版本'),
    StructureAttribute(attr_name='ip', attr_description='IP地址')
]

Structure.objects(name=server.name).update_one(description=server.description, attributes=server.attributes)

mysql = Structure()
mysql.name = 'mysql'
mysql.description = 'MySQL数据库'
mysql.attributes = [
    StructureAttribute(attr_name='ip', attr_description='IP地址'),
    StructureAttribute(attr_name='port', attr_description='端口'),
    StructureAttribute(attr_name='x_port', attr_description='x协议端口'),
    StructureAttribute(attr_name='major_version', attr_description='主版本号')
]

Structure.objects(name=mysql.name).update_one(description=mysql.description, attributes=mysql.attributes)
