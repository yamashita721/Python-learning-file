# validate user input excercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("enter your username: ")


if len(username) >12:
    print("your username can't be of more than 12 characters.")
elif not username.find(" ") == -1:  # used this to check wheather is input contains spaces or not
    print("your username can't contain spaces. ")
elif not username.isalpha():
    print("your user name can't contain numbers.")
else:
    print(f"welcome {username}")