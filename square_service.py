import math

def sqr_svc():
  num = 0
  perfect_num = math.sqrt(num)
  a = 2
  b = 1.0

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
