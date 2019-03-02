def isPrime(num):
    counter = 0
    for i in range(1, int(num + 1)):
        if (i > num):
            break

        if (num % i == 0):
            counter = counter + 1

    if (counter == 2):
        return 1
    else:
        return 0
