# Count down timer
import time

#time.sleep(3)
#print("TIME'S UP!")
#() --> parentheses or round

my_time = int(input("Enter the time in seconds:  "))

for x in range(my_time,0 ,-1):
    # this form is called step , also we can use reverse function
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("TIME'S UP!")

