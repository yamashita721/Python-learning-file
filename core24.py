# while loop:

food = input("Enter a food you like ( q to quit):  ")

while not food == "q":
    print(f"YOU LIKE {food}😋")
    food = input("Enter an another food you like ( q to quit):  ")

print("BYE")
