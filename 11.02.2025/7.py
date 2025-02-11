#dekorator - zmieniaja zachowanie funkcji, dekorator to inna funkcja
# po co? ay zrobic rozne warianty funkcji

def my_dekorator(fn):
    def wraper():
        print('Początek odliczania')
        fn()
        print('koniec odliczania')
    return wraper

def get_5_values():
    for v in range(1,6):
        print(v)
get_5_values_decorate = my_dekorator(get_5_values)
get_5_values_decorate()