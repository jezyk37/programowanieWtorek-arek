#tuple - jest to typ niemutowany
mojatupla = (1,2,3,4,5,'S',True,'Arkadiusz lubi burgery z bonjo Chopie')
#mojatupla[0] = 20
print(mojatupla[5])
print(len(mojatupla)+ 10 - 1 * 12)

lista = [1,2,3,4,5,6]
tubla_moja = tuple(lista)
print(tubla_moja)
print(max(tubla_moja))
print(min(tubla_moja))
print(sum(tubla_moja))
a,b,c,d,e,f = lista
print(a)