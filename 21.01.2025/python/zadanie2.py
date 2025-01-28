'''
print(1 == 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(1 != 2)

a = 'a'
b = 'b'
c = (a==b)
print(c)
'''

if 1==1:
    print("ok")
else:
    print("nie ok")

if 1==1:
    print("ok")
elif 2==2:
    print("ok")
else: 
    print("nie ok")

name = input("Podaj imie = ")
if len(name) < 3:
    print("Imie musi miec co najmniej 3 znaki") 
else:
    print(name)

a = 'aaa'
if not a:
    print("nie istnieje")