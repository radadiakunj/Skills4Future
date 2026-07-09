def dictionary_methods_demo():
    print("\n--- Dictionary: 5 methods ---")
    student = {"name": "Kunj", "age": 21, "city": "Ahmedabad"}

    print("1) get:", student.get("name"))
    print("2) keys:", list(student.keys())) # To get the genres of keys in the dictionary
    print("3) values:", list(student.values())) # To get the genres of values in the dictionary
    print("4) items:", list(student.items()))
    print("5) pop('city'):", student.pop("city"))
    print("After pop:", student)


def list_methods_demo():
    print("\n--- List: 5 methods ---")
    numbers = [10, 20, 30]

    numbers.append(40)
    print("1) append(40):", numbers)

    numbers.extend([50, 60])
    print("2) extend([50, 60]):", numbers)

    numbers.insert(1, 15)
    print("3) insert(1, 15):", numbers)

    numbers.remove(30)
    print("4) remove(30):", numbers)

    popped = numbers.pop()
    print("5) pop():", popped, "| Remaining:", numbers)


def tuple_methods_demo():
    print("\n--- Tuple: 5 useful operations/methods ---")
    data = (2, 4, 6, 4, 8)

    print("1) count(4):", data.count(4)) # To count the number of occurrences of an element in a tuple
    print("2) index(6):", data.index(6)) # To find the index of an element in a tuple
    print("3) len(data):", len(data)) # To find the length of a tuple
    print("4) slicing data[1:4]:", data[1:4])
    print("5) membership 8 in data:", 8 in data) # To check if an element is in a tuple


def set_methods_demo():
    print("\n--- Set: 5 methods ---")
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    s1.add(6)
    print("1) add(6):", s1)

    s1.update([7, 8])
    print("2) update([7, 8]):", s1)

    print("3) union(s2):", s1.union(s2))
    print("4) intersection(s2):", s1.intersection(s2))
    print("5) difference(s2):", s1.difference(s2))


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

    print("\n3) if-elif-else with one loop:")
    for marks in [35, 72, 91]:
        if marks >= 90:
            print(marks, ": Grade A")
        elif marks >= 60:
            print(marks, ": Grade B")
        else:
            print(marks, ": Grade C")

    print("\n4) Nested if-else with one loop:")
    for age in [16, 22]:
        if age >= 18:
            if age >= 21:
                print(age, ": Adult and can drive")
            else:
                print(age, ": Adult but learning phase")
        else:
            print(age, ": Minor")


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


if __name__ == "__main__":
    dictionary_methods_demo()
    list_methods_demo()
    tuple_methods_demo()
    set_methods_demo()
    if_statements_demo()
    break_continue_pass_demo()
    # input_method_demo()  # Uncomment to run interactive input example
    range_len_type_demo()
    loops_demo()
