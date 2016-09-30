fobj = open("sample.txt")
#print fobj.read()
''' If you call read() again it will return empty string as it already read the whole file. readline() can help you to read one
line each time from the file.'''
print fobj.readline()

fobj.close()