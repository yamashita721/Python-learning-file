#type casting: the process of converting a variable from one data type to another
str(), int(), float(), bool()
#type casting is especially useful for handling user's data



name="yamashita"
age= 19
gpa=9.9
is_student=True

print(type(is_student))


#now we will type one data type to another

#lets convert gpa to a float

gpa= int(gpa)

print(gpa)

name = bool(name)

print(name)


age=float(age)
print(age)

