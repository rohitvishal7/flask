def hello(*, name='User'):
    print("Hello %s" % name)
#hello('Kushal')
'''Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: hello() takes 0 positional arguments but 1 was given'''
hello(name='Kushal')