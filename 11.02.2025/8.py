#dekorujemy za pomoca @

def my_dekorator(fn):
    def wraper():
        print('Początek odliczania')
        fn()
        print('koniec odliczania')
    return wraper

@my_dekorator
def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values(0)