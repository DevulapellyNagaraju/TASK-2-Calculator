from calculator_functions import add, subtract, multiply, divide, display_result

print("""
+-------------------------------------+
|    Welcome to Simple Calculator!    |
+-------------------------------------+ 
""")

while True:
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            display_result(num1, num2, '+', result)
        elif choice == '2':
            result = subtract(num1, num2)
            display_result(num1, num2, '-', result)
        elif choice == '3':
            result = multiply(num1, num2)
            display_result(num1, num2, '*', result)
        elif choice == '4':
            result = divide(num1, num2)
            display_result(num1, num2, '/', result)

        continue_choice = input("Want to continue (y/n) ? ")
        if continue_choice.lower() != 'y':
            print("Exiting the program. Goodbye!")
            break

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid option.")
