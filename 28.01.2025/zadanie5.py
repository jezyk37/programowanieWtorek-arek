# napisz app na bazie funkcji:
# wyznacz pole trojkata z herona
# przekz liste argumentow nieskonczona: wyznacz ume, srednia,min i max

import math



def fn(a, b, c):
    p = (a + b + c) / 2
    heron = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(heron)

fn(3,4,5)

def fn1(*args):
    print(max(args))
    print(min(args))
    print(sum(args))
    print(len(args))

fn1(1,2,3,4,5,6,7,8,9)


