import math

def quad_func():
    # Intro
    print("Quadtic equation formula: ")
    print("ax^2 + bx + c = 0")
    print("If any of variables doesn't exist, set it to 0 \n")

    a = input("a = ")
    b = input("b = ")
    c = input("c = ")


    try:
        a = float(a)
        b = float(b)
        c = float(c)

    except ValueError:
        print.err("[!] At least one of the inputted variables is not a number")

    # Obliczonka

    if (a == 0):
        # There is no sens to calculate value of delta
        # There are no roots
        # There is no axis of symmetry because graph is a straight

        function = str(b) + "x " + "+ " + str(c)
        apex = "Graph is a straight - there is no apex"
        range = "Graph is a straight, y = " + str(c)



    else:
        delta = (math.pow(b,2) - 4 * a * c)
        p = -b / (2*a)
        q = -delta / (4*a)
        function = str(a) + "x^2" + " + " + str(b) + "x " + "+ " + str(c)
        apex = "A(" + str(p) + ", " + str(q) + ")"
        range = ""

    if (a < 0):
        range = ("-Infinity," + str(q) + ")")
    elif (a > 0):
        range = "(" + str(q) + ", +Infinity)"


    if (a!= 0):

        if (delta == 0):
            x0 = -1 * (b / (2*a))
        elif (delta > 0 ):
            x1 = ((-b - math.sqrt(delta) / (2*a)))
            x2 = ((-b + math.sqrt(delta) / (2*a)))

      # **PRINTER**

    print("Your function: " + str(function))
    print("Apex: " + str(apex))

    if (a != 0):
        print("Delta: " + str(delta))
        print("Domain of a function: R" + str(range));
        print("Axis of symmetry of parabola: x = " + str(p))

        if (delta < 0):
            print("Roots: There are no roots")
        elif (delta == 0):
            print("Roots: x0 = " + str(x0))
        elif (delta > 0):
            print("Roots: x1 = " + str(x1) + ", x2 = " + str(x2))

        if (a < 0):
            print("Highest magnitude: " + str(q) + ", for x = " + str(p))
            print("Lowest magnitude: Does not exist")
            # !! patrz linia 85
            print("Monotonicity: ")
            print("Function increasing in range: " + ("(-Infinity, " + str(p) + ">"))
            print("Function decreasing in range:  " + ("<" + str(p) + ", +Infinity)"))

        elif (a > 0 ):
            print("Highest magnitude: Does not exist")
            print("Lowest magnitude: " + str(p) + ", for x = " + str(q))
            print("Function increasing in range: " + ("<" + str(p) + ", +Infinity)"))
            print("Function decreasing in range: " + ("(-Infinity" + ", " + str(p) + ">"))
    elif (a == 0):
        print("Range: " + str(range))
        print("Roots: There are no roots")
        print("There is no axis of symmetry because graph is a straight")