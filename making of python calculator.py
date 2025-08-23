# Python Calculator
# .strip() removes any extra spaces which causes errors in code

while True:
    operator = input("enter an operator  (+ - * /)").strip()
    num1 = float(input("enter 1st number"))
    num2 = float(input("enter 2nd number"))

    if operator == "+":
        result = num1 + num2
        print(result)
        choice = input("do you want to contiue? (yes/no): ")
        if choice.lower() == "no":
            break
    elif operator == "-":
        result = num1 - num2
        print(result)
        choice = input("do you want to contiue? (yes/no): ")
        if choice.lower() == "no":
            break
    elif operator == "*":
        result = num1 * num2
        print(result)
        choice = input("do you want to contiue? (yes/no): ")
        if choice.lower() == "no":
            break
    elif operator == "/":
        result = num1 / num2
        print(result)
        choice = input("do you want to contiue? (yes/no): ")
        if choice.lower() == "no":
            break
    else:
        print("invalid operator")

