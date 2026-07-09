def if_statements_demo():
    print("\n--- If / If-Else / If-Elif-Else / Nested If-Else ---")

    print("\n1) Simple if with one loop:")
    for n in [5, 12, 7]:
        if n > 10:
            print(n, "is greater than 10")

    print("\n2) if-else with one loop:")
    for n in [3, 8]:
        if n % 2 == 0:
            print(n, "is even")
        else:
            print(n, "is odd")
          
def break_continue_pass_demo():
    print("\n--- break / continue / pass ---")

    print("\n1) break example:")
    for i in range(1, 6):
        if i == 4:
            print("Stopping at", i)
            break
        print(i)

    print("\n2) continue example:")
    for i in range(1, 6):
        if i == 3:
            continue
        print(i)

    print("\n3) pass example:")
    for i in range(1, 4):
        if i == 2:
            pass  # Placeholder: no action for this condition
        print(i)


def input_method_demo():
    print("\n--- Input method example ---")
    name = input("Enter your name: ")
    print("Hello,", name)


def range_len_type_demo():
    print("\n--- range / len / type examples ---")
    print("range(1, 6):", list(range(1, 6)))

    text = "Python"
    print("len('Python'):", len(text))

    value = 10.5
    print("type(10.5):", type(value))


def loops_demo():
    print("\n--- for loop / while loop examples ---")

    print("For loop:")
    for fruit in ["apple", "banana", "mango"]:
        print(fruit)

    print("While loop:")
    count = 1
    while count <= 3:
        print("count =", count)
        count += 1
