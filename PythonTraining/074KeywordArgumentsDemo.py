def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(12, 24)
# a is 12 and b is 24 and c is 10

func(12, c = 24)
# a is 12 and b is 5 and c is 24
func(b=12, c = 24, a = -1)
# a is -1 and b is 12 and c is 24