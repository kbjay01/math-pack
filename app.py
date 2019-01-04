import quadratic_function,segment_length

print("What do you want to do?")
print("1. Let's calculate quadratic_function")
print("2. Let's calculate length of a segment")
choice = input(">> ")

if choice == "1":
    quadratic_function.quad_func()
elif choice == "2":
    segment_length.lenSeg()
 else:
    print("[!] Unknown choice")
