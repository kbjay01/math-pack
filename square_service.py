import math
def sqr_svc(num):

  perfect_num = math.sqrt(num)
  a = 2.0
  b = 1.0
  while (True):

    if (a * math.sqrt(b) < perfect_num):
      b += 1

    if (a * math.sqrt(b) > perfect_num):
      a += 1
      b = 1

    if (a * math.sqrt(b) > (perfect_num)) and b == 1:
      return num
      break

    if (a * math.sqrt(b) == perfect_num):
      output = str(int(a)) + chr(8730) + str(int((b)))
      return output
