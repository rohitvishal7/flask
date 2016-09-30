def read_file():
    f = open('abc.txt', 'r')
    print('File contents: ' + f.read(7))
    #lines = f.readlines()
    #print(lines)
    f.close()

def write_file():
    f = open('abc.txt', 'a')
    f.write('I am a winner')
    f.close()

def read_write_file():
    f = open('abc.txt', 'a+')
    print('Initial tell: ', f.tell())
    f.write('I am a winner')
    f.seek(3)
    print('Again tell: ', f.tell())
    print('Read file: ', f.read())
    
#read_file()
#write_file()
read_write_file()
