# Variable : A variable is a container for value( string, integer, float , boolean)
#            A variable behaves as if it was a value of it's contains
from CORE4 import is_student

#strings
first_name="yamashita"
food="pizza"
email="yamashita@fake.com"
say="hey"


print(f"hello {first_name}")
print(f"you like {food}")
print(f"your email is {email}")
print(f"{say}")

#integers


age=19
standard=6
quantity = 9

print(f'you are {age}')
print(f"you are in {standard} standard")
print(f"how many apples do you have?: {quantity}")

# float = it's kind of decimal thing

price = 4.7
gpa = 9.99

print(f"how much is it for?: {price}")
print(f"how much score do u get?: {gpa}")


# boolean = it's either True or False(ALSO IN THIS THE FIRST LETTER OF TRUE OR  FALSE SHOULD BE CAPITAL)


is_student = True
for_sale = False

if for_sale:
    print(f"this cloth is on sale: {for_sale}")
else:
    print(f"it's not on sale: {for_sale}")
