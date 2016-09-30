a = 'Fedora', 'Debian', 'Kubuntu', 'Pardus'
print a
#('Fedora', 'Debian', 'Kubuntu', 'Pardus')

print a[1]
# 'Debian'

for x in a:
    print(x)
#Fedora Debian Kubuntu Pardus


#Tuples are immutable
del a[0]