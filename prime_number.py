p_num = 0
isPrime = 0
def prime_numb():
    counter = 0 
    for i in range(1,p_num):
        if (i>p_num):
            break;

        if (p_num%i == 0):
           counter = counter + 1
    if (counter == 2):
        isPrime = 1
    else:
        isPrime = 0
  
