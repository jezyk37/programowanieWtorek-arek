# listy - mozemy modyfikowac, sa mutowalne

'''
mojalista = [1,2,3,4,5,6,'S','a','arek',True,False]
print(mojalista[4])
mojalista[0] = 25
print(mojalista)
mojalista.append('Lubie programowac')
print(mojalista)
print(mojalista[0:5])
print(mojalista[5:])
'''

'''
lista1 = [1,2,3,4,5]
lista2 = [2,3]
lista3 = lista1 + lista2
print(lista3)
print(3 in lista1) #przeszukanie listy
print(len(lista3))
'''

mojesuperlista = [zmienna for zmienna in range(10)] #list comprehension
print(mojesuperlista)
mojesuperlista2 = [zmienna for zmienna in range(9,27) if zmienna % 2 == 0]
print(mojesuperlista2)