def calculation(choice, first_number, second_number):

    if choice == "+":
        result = first_number + second_number
    elif choice == "-":
        result = first_number - second_number
    elif choice == "*":
        result = first_number * second_number
    elif choice == "/":
        result = first_number / second_number
    elif choice == "^":
        result = first_number ^ second_number
    elif choice == "%":
        result = first_number % second_number
    else:
        result = "Unrecognized operation"

    return result

def select_op(choice):

    display_result = -1

    if choice == "#":
        return display_result
    elif choice == "$":
        return 1
    else:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        result = calculation(choice, first_number, second_number)

        if result == "Unrecognized operation":
            print("Unrecognized operation")
        else:
            print(first_number, choice, second_number, "=", result)

while True:
    print("Select operation.")
    print("1.Add       : + ")
    print("2.Subtract  : - ")
    print("3.Multiply  : * ")
    print("4.Divide    : / ")
    print("5.Power     : ^ ")
    print("6.Remainder : % ")
    print("7.Terminate : # ")
    print("8.Reset     : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
        


