a = 3
b = 4
def fn():
    return 10
#print(type(a))
#print(id(a), id(b))
#print(dir(a))
a = fn
print(dir(fn))
print(dir(a))