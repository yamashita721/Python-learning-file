# python weight convertor

weight = float(input("enter your weight: "))
unit = input("kilograms or pounds? k or l : ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is : {round(weight, 1)} {unit} ")
elif unit == "l":
    weight = weight/2.205
    unit = "kgs."
    print(f"your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid!")


