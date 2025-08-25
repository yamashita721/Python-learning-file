# Python compound interest calculator
# A = P(1+R/N)^t
# WHERE; A = final amount , P = initial principle balance , r = intrest rate, t = number of time periods elapsed


principle = 0
rate = 0
time = 0
while principle<=0:
    principle = float(input("Enter the principal amount: "))
    if principle<=0:
        print("Principle can't be less than or equal to zero")

while rate<=0:
    rate = float(input("Enter the rate: "))
    if rate<=0:
        print("Interest rate can't be less than or equal to zero")

while time<=0:
    time = float(input("Enter the time amount: "))
    if time<=0:
        print("time can't be less than or equal to zero")

#print(principle)
#print(rate)
#print(time)

total = principle *pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")