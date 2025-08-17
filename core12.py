# IF = do some code IF some condition is True
#       Else do something else

age = int(input("enter your age: "))

if age>= 100:
    print(f"you are too old too sign up")
elif age>=18:
    print(f"you are signed up.")
elif age<0:
    print(f"you are not born yet.")
elif age<18:
    print(f"you must be 18+ to sign up.")

else:
    print(f"you are not eligible for sign up.")