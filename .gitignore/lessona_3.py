# Count odd and even numbers.  Count odd and even digits of the whole number. 
# E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5)

whole_number = 34560
evenum = []
oddnum = []


while(whole_number):
    result1 = whole_number % 10 
    if ((result1 % 2) == 0):
        evenum.append(result1)
    else:
        oddnum.append(result1)
    whole_number = whole_number // 10
print("Even numbers")
print(evenum)
print("Total number of even numbers is:")
print(len(evenum))

print("Odd Numbers")
print(oddnum)
print("Total number of odd numbers is:")
print(len(oddnum))

