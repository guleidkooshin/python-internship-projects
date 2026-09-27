def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Maths error"
    return a / b


num1 = float(input("Enter number 1: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter number 2: "))


if operator == "+":
    result = add(num1, num2)

elif operator == "-":
    result = subtract(num1, num2)

elif operator == "*":
    result = multiply(num1, num2)

elif operator == "/":
    result = divide(num1, num2)

else:
    result = "Invalid operator"


print("Result:", result)