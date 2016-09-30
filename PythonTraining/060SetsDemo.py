a = set('abracadabra')
b = set('alacazam')
c= set (['Onkar','Amit'])

print a # unique letters in a
#{'a', 'r', 'b', 'c', 'd'}
print c

print a - b # letters in a but not in b
#{'r', 'd', 'b'}

print a | b # letters in either a or b
#{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

print a & b # letters in both a and b
#{'a', 'c'}

print a ^ b # letters in a or b but not both
#{'r', 'd', 'b', 'm', 'z', 'l'}

a.discard('d')
print 'updated ',a