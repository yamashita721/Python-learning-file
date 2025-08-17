
response = input("would you like some food? (y/n): ")


if response == "y":
    print("have some food.")
else:
    print("no food for you.")


#another example
name = input("enter your name: ")

if name == "":
    print(f"you did not type your name. ")
else:
    print(f"hello {name}")