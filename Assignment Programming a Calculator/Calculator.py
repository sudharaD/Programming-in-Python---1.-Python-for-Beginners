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
            def validate_only_integer(number):
                try:
                    return float(number)
                except ValueError:
                    return "not an integer!"
            
            # validate "$" character
            def reset_character_validate(number):
                if "$" in number:
                    return "reset"
            
            first_number = input("Enter first number: ")
            print(first_number)
            if reset_character_validate(first_number) == "reset":
                return 1

            validated_first_number = validate_only_integer(first_number)
            if validated_first_number == "not an integer!":
                print("not an integer!")
                return 1
            else:
                # print(int(validated_first_number))
                second_number = input("Enter second number: ")
                print(second_number)
                if reset_character_validate(second_number) == "reset":
                    return 1

                validated_second_number = validate_only_integer(second_number)
                if validated_second_number == "not an integer!":
                    print("not an integer!")
                    return 1
                # else:
                #     print(int(validated_second_number))

            result = calculation(choice, validated_first_number, validated_second_number)

            if result == "Unrecognized operation":
                print(result)
            elif result == "Something Went Wrong":
                print(result)
            else:
                print(validated_first_number, choice, validated_second_number, "=", result)

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
        


