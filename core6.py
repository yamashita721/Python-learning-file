#excercise : rectangle area calculation ( area = l*b)
#for writing area unit centimeter sqare we use: num lock on + alt+ 0178

length=float(input("enter the length"))

width=float(input("enter the width"))

area= length*width

print(f"the area of rectangle is: {area} cm²")

#excersie 2: shopping cart program

item= input("what would you like to buy?:")
price= float(input("what is the price?:"))
quantity= int(input("how much would you like to buy?:"))
total= price * quantity

print(total)
print(f"your total is ${total}")

#this is how we accept users input in python