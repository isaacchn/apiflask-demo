from run_create_instance_v2 import create_sub_class_from_name, create_class_from_name

HostClass = create_class_from_name('host')
LinuxHostClass = create_sub_class_from_name(HostClass, 'linux_host')

for obj in HostClass.objects():
    print(obj.hostname)

print('-----')

for obj in LinuxHostClass.objects():
    print(obj.hostname)
