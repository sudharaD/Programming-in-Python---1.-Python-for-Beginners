def calculation(choice, first_number, second_number):

    if choice == "+":
        result = first_number + second_number
    elif choice == "-":
        result = first_number - second_number
    elif choice == "*":
        result = first_number * second_number
    elif choice == "/":
        if second_number == 0:
            print("float division by zero")
            return "None"
        else:
            result = first_number / second_number
    elif choice == "^":
        result = first_number ^ second_number
    elif choice == "%":
        if second_number == 0:
            print("float division by zero")
            return "None"
        else:
            result = first_number % second_number
    else:
        result = "Unrecognized operation"

    return result

def select_op(choice):

    display_result = -1

    if choice not in ("+", "-", "*", "/", "^", "%", "#", "$"):
        print("Unrecognized operation")
    else:
        if choice == "#":
            return display_result
        elif choice == "$":
            return 1
        else:
            
            # validate input only numbers
            def validate_only_intrger(number):
                try:
                    number = float(number)
                except ValueError:
                    print(number, "not an integer!")
                    return 1
            
            first_number = float(input("Enter first number: "))
            validate_only_intrger(first_number)
            print(int(first_number))
            second_number = float(input("Enter second number: "))
            validate_only_intrger(second_number)
            print(int(second_number))

            result = calculation(choice, first_number, second_number)

            if result == "Unrecognized operation":
                print(result)
            elif result == "Something Went Wrong":
                print(result)
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
        


