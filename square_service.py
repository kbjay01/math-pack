import math

perfect_num = 0
a = 1.0
b = 1.0

def sqr_svc():
    while (True):

        if (a * math.sqrt(b) < perfect_num):
            b = b + 1

        elif (a * math.sqrt(b) > perfect_num):
            a = a+1
            b = 1

        elif (a * math.sqrt(b) == perfect_num):
            if a == 1:
                a = 2

    a = str(a)
    b = str(b)