import math

num = 0
a = 2.0
b = 1.0
def sqr_svc():

  perfect_num = math.sqrt(num)
  while (True):

    if (a * math.sqrt(b) < perfect_num):
        b = b + 1
        #print("if pierwszy")

    if (a * math.sqrt(b) > perfect_num):
        a = a+1
        b = 1
        #print(str(a) + "," + str(b))

    if (a * math.sqrt(b) == perfect_num):
        break

  print(str(a) + "√" + str(b))
