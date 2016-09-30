import pickle

def pickle_file():
    f = open('lists.dat', 'ba')
    companylist = ['Xoriant', 'TCS', 'Infosys']
    pickle.dump(companylist, f)
    print('pickled companylist')

def unpickle_file():
    f = open('lists.dat', 'br')
    
    #my_list = pickle.loads(f)
    #print('my_list = ', my_list)
    my_company_list = pickle.load(f)
    print('type of my_company_list: ', type(my_company_list))
    my_company_list_2 = pickle.load(f)
    print('tell_2: ', f.tell())
    print('my_company_list: ', my_company_list)
    print('my_company_list_2: ', my_company_list_2)
    
#pickle_file() 
unpickle_file()   