# Python Calculator
# .strip() removes any extra spaces which causes errors in code

while True:
    operator = input("enter an operator  (+ - * /): ").strip()

    try:
        num1 = float(input("enter 1st number: "))
    except ValueError:
        print("that's not an valid operator1! try again.")
        continue

    try:
        num2 = float(input("enter 2nd number: "))
    except ValueError:
        print("that's not an valid operator! try again.")
        continue





    if operator == "+":
        result = num1 + num2
        print(result)

    elif operator == "-":
        result = num1 - num2
        print(result)

    elif operator == "*":
        result = num1 * num2
        print(result)

    elif operator == "/":
        result = num1 / num2
        print(result)

    else:
        print("invalid operator")
        choice = input("do you want to contiue? (yes/no): ")
        if choice.lower() == "no":
            break

