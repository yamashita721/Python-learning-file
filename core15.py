# python weight convertor

weight = float(input("enter your weight: "))
unit = input("kilograms or pounds? K or L : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is : {round(weight, 1)} {unit} ")
elif unit == "L":
    weight = weight/2.205
    unit = "kgs."
    print(f"your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid!")


