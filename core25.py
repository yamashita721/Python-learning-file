# while loop

num = int(input("Enter a num between 1-10: "))

while num<1 or num>10:
    print(f"{num} is not valid!")
    num = int(input("Enter a num between 1-10: "))# from 3 examples we are this here again and again to escape the loop
else:
    print(f"Your number is {num}")



    # we can even directly write print statement without writing else!🪐


