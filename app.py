import quadratic_function,segment_length

def main_menu():
    print("What do you want to do?")
    print("1. Let's calculate quadratic function")
    print("2. Let's calculate length of a segment")
    choice = input(">> ")

    if choice == "1":
        quadratic_function.quad_func()
    elif choice == "2":
        segment_length.len_seg()
    else:
        print("[!] Unknown choice \n----------\n")
        main_menu()

main_menu()
