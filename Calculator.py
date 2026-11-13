def calculator():
    print("\n================================")
    print("       SMART CALCULATOR")
    print("================================")

    history = []

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '7':
            print("\nThank you for using calculator!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                operation = "Addition"

            elif choice == '2':
                result = num1 - num2
                operation = "Subtraction"

            elif choice == '3':
                result = num1 * num2
                operation = "Multiplication"

            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
                operation = "Division"

            elif choice == '5':
                if num2 == 0:
                    print("Cannot calculate modulus by zero!")
                    continue
                result = num1 % num2
                operation = "Modulus"

            elif choice == '6':
                result = num1 ** num2
                operation = "Power"

            print("\nResult:", result)

            history.append(
                operation + ": " + str(num1) +
                " and " + str(num2) + " = " + str(result)) )

        except ValueError:
            print("Please enter valid numbers.")

        print("\nCalculation History:")
        for item in history:
            print(item)


calculator()
              
