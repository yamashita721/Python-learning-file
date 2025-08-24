# Tempreture conversion programme

while True: #used it for making loop
    unit = input("is this tempreature in celcius or fahrenheit (c/f): ").strip().lower()
    temp = float(input("enter the tempreture: "))




    if unit == "c":
        temp = (9 * temp / 5 + 32)
        print(f"the tempreture in fahrenheit is: {temp} °f") # for bringing degree used alt + 0176


    elif unit == "f":
        temp = (temp - 32) * 5 / 9
        print(f"the temperature in celcius is: {temp}°c")

    else:
        print(f"{unit} is not an valid measurment.")

    choice = input("do you want to continue?: (yes/no) ").strip().lower()
    if choice.lower() == "no":
        break # last three lines for asking choices and breaking loop

# .strip() -- it helps to avoid issue of some extra spaces
# .lower() -- it was used so that even wif type captial or small
# c or f code works
# we could have also added error handling for tempreture input
# will add that later on
