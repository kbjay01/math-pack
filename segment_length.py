import math, prime_number, square_service

def len_seg():

    print("Segment has two points")
    print("A[x1,y1]")
    print("B[x2,y2]")
    print("Insert the data")
    x1 = input("x1 = ")
    y1 = input("y1 = ")
    x2 = input("x2 = ")
    y2 = input("y2 = ")

    try:
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
    except ValueError:
        print("[!] At least one of the inputted variables is not a number")
        exit()

    seg_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("test " + str(seg_length ** 2))
    prime = prime_number.isPrime(int(seg_length))
    print(prime)

    if prime == 0:
        print("Length of this segment: " + str(seg_length))
        print("Or just simply...")
        root = str(square_service.sqr_svc(float(seg_length ** 2)))

        if (str(int((float(seg_length ** 2)))) in root):
            print(chr(8730) + str(int(seg_length ** 2)))
        else:
          print(root)

    if prime == 1:
        print("Length of this segment: " + str(seg_length))
        print("Or " + chr(8730) + str(int(seg_length ** 2)))
