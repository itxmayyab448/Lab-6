import math

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, **, //, sqrt): ")

if operator == "sqrt":
    if num1 < 0:
        print("Error: Cannot take square root of a negative number!")
    else:
        print("Result:", math.sqrt(num1))
else:
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif operator == "%":
        if num2 == 0:
            print("Error: Cannot take modulus by zero!")
        else:
            print("Result:", num1 % num2)

    elif operator == "**":
        print("Result:", num1 ** num2)

    elif operator == "//":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 // num2)

    else:
        print("Invalid operator! try again")