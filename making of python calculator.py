# Python Calculator
#strip() removes any extra spaces which causes errors in code


operator = input("enter an operator( +, -, *, /)").strip()
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))


if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

