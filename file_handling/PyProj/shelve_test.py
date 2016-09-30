import shelve

def shelve_write_file():
    f = shelve.open('shelve_data.dat')
    f['1.id'] = 101
    f['1.name'] = 'Tom'
    f['salary_2'] = 10000
    #f.close()
    print('Shelve done')

def shelve_read_file():
    f = shelve.open('shelve_data.dat')
    print('f type: ', type(f))
    mydict = dict(f)
    print(f)
    accno = f['id']
    name = f['name']
    salary = f['salary']
    #print(accno, ' - ', name, ' - ', salary)

#shelve_write_file()
shelve_read_file()