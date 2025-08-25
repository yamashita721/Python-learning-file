
response = input("would you like some food? (y/n): ")

# we used here double equal sign to check double condition
# since equal sign used as assingment operator!
if response == "y":
    print("have some food.")
else:
    print("no food for you.")


#another example
name = input("enter your name: ")

while True:
    if name == "":
        print(f"you did not type your name. ")
        name = input("enter your name: ")
    else:
        print(f"Hello {name}")
        break
