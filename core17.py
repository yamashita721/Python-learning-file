# logical operators = evaluate multiple conditions (or ,and , not)
#                     or = at least one condition must be true( then entire statement is true)
#                     and = both conditions must be true
#                     not = inverts the conditions ( not false , not true)

#temp = -5
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
 #   print("The outdoor event is cancelled.")
#else:
 #   print("The outdoor event is still scheduled.")


# Let's try and operator
#temp = 5
#is_sunny = True

#if temp >= 30 and is_sunny:
 #   print("It's HOT outside 🥵")
  #  print("It's SUNNY too☀️")
#elif temp <= 0 and is_sunny:
 #   print("It's COLD outside🥶")
  #  print("It's SUNNY too☀️")
# else:
 #   print("you are dumb🤷‍♀️")

 # Let's try not operator

temp=32
is_sunny = False

if temp > 28 and not is_sunny:
     print("it's hot")
     print("and it's cloudy☁️ too")
     # that's how we use not operator