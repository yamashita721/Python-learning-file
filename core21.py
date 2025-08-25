# string indexing = accessing elements of a squence using []
#            [start : end : step]
# the first index is zero because computers always starts from zero
from ctypes import HRESULT

credit_number = "5489-4545-5878-4585"

#print(credit_number[4])

#print(credit_number[0:4]) # here we wanted indexing from start till 4

#print(credit_number[5:9]) # midones as iniated
#print(credit_number[5:])
#print(credit_number[-1])

# step:
#print(credit_number[::2])# with this we can get every 2nd place of the credit card number

# get last 4 digit of a credit card number
#last_digits = credit_number[-4:]
# you know what we can reverse the credit card number
result = credit_number[::-1]

print(result)



