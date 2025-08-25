# conditional operator = A one line shortcut for the if-else statement (ternary operator)
#                        print or assign one of the two values based on a condition
#                        "X" if condition else "Y"


#while True:
 #   num = int(input("enter a number: "))

  #  if num > 0:
   #     print('positive')
    #elif num == 0:  # see here i was using quotation which was making it string intead of int so i removed it
     #   print("zero")

    #else:
     #   print("dumb, learn number system. 🧹")
# for else statement to work type negative number
        # ask user if they want to continue

   # choice = input("do u wanna continue? (yes/no):")
    #if choice.lower() == "no":
     #   print("okay , please try back again someday😁")
      #  break

# Let's try one line else if statement

num = 8
a = 7
b = 5
age = 19

#print("positive" if num > 0 else "negative")
#result = "EVEN" if num % 2 == 0 else "OOD" # % modulus function which gives remainder
#max_num = a if a > b else b
#min_num = a if a < b else b

status = "adult" if age>= 18 else "child"

print(status)

