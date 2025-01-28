def fn(a,b):
    print('to jest fn', a+b)

#fn(2,3)
#fn(4,6)

def fn1(x=1,g=5):
    print('To jest deafult = ', x+g)

#fn1(30,4)

def fn2(a,b=0,c=0):
    print('a = ', a, 'b = ', b, 'c = ', c)

fn2(2,c=20,b=3)