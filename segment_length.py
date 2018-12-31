import math,prime_number,square_service

def lenSeg():
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
        print.err("[!] At least one of the inputted variables is not a number")
        return

    seg_length = math.sqrt((math.pow(x1-x2,2)) + math.pow(y2-y1,2))
    prime_number.p_num = seg_length
    prime_number.prime_numb()

    if prime_number.p_num == 1:
        square_service.perfect_num == seg_length
        square_service.sqr_svc()
        print("Length of this segment: " + str(seg_length))
        print("Or just simply...")
        seg_length = str(seg_length)
        seg_length = square_service.a + "√" + square_service.b
        print(seg_length)