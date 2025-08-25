#input= a function that prompts the user to enter data
#       Returns the entered data as a string


age=int(input("what is your age?:")) # we used type casting here to change string into integer
name=input("what is your name?:")

age= age+ 1
# so strings we can mathematically use but we would have to type cast it into
#to an integer or a float
#however we can skip some step's: by taking up an extra line , we can put the int() function instead see above example
# after removing the type casting of age=int(age)

print(f"hey {name}!")
print("Happy birthday🥳")
print(f"now you're 20.")