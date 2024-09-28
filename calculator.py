#  Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x // y

while True:
    print("\n--- Extended Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (Remainder)")
    print("6. Exponentiation (Power)")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("Choose an operation (1-8): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue  # Ask again if the input is not a number

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")

        elif choice == '5':
            result = modulus(num1, num2)
            print(f"The result of {num1} % {num2} (remainder) is: {result}")

        elif choice == '6':
            result = exponentiate(num1, num2)
            print(f"The result of {num1} ^ {num2} (power) is: {result}")

        elif choice == '7':
            result = floor_divide(num1, num2)
            print(f"The result of {num1} // {num2} (floor division) is: {result}")

    elif choice == '8':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice, please choose a valid operation.")
