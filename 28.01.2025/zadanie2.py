def fn(a,*args): #gwaizda oznacza niekonczaca sie ilosc elementow
    #**dict_args - zostanie zebrane arg do slownika jako klucz-wartosc
    print(a,args)
    for el in args:
        print(el)

#fn(2,3,4,5,6,7,8,3,True, 'Arkadiusz', 'cx')
def fn2(a,*args,**dict_args):
    print(a)
    print(args)
    print(dict_args)
    for elarg in args:
        print(elarg)
    for key in dict_args:
        print(dict_args[key])

fn2(3,'Arek','lubi','3ct',1,2,3,4,True,user='admin',version=1.0,db='sql')