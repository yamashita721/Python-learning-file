#excercise : rectangle area calculation ( area = l*b)
#for writing area unit centimeter sqare we use: num lock on + alt+ 0178
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))


area= length * breadth
print(f"the area of rectangle is: {round(area,3)} cm²")

#excersie 2: shopping cart program

item= input("what would you like to buy?:")
price= float(input("what is the price?:"))
quantity= int(input("how much would you like to buy?:"))
total= price * quantity

print(f"your total is ${total}")

#this is how we accept users input in python