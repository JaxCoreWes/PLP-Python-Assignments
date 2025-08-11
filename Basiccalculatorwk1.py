num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operator.")

