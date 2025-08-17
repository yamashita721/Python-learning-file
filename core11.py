# excercise : calc. hypotenuse of a right angle traingle ( a^2 + b^2 = c^2)

import math

a = float(input("enter side a : "))
b = float(input("enter side b : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side c is : {c}")