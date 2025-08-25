# format specifiers = {value:flags} format a value based on what flags are inserted
#                           flags are inserted


# .(number)f = round to that many decimal places ( fixed point)
# :(number) = allocate that many spaces
# :o3 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ =  center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma seperator

price1 = 35998.14159
price2 = -95645.65
price3 = 1254.34

#print(f"Price 1 is ${price1: .3f}")
#print(f"Price 2 is ${price2: .3f}")
#print(f"Price 3 is ${price3: .3f}")
# u can even try with differ. examples like .1f or .2f (here f is float)

#print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price1: >10}")
#print(f"Price 3 is ${price1:10}")
# these are for giving spaces like we wrote so it gave 10 spaces after every price

print(f"Price 1 is ${price1:,}")
#print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3: }")
# so this way u can try all above flags!