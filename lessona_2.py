# Find max number from 3 values, entered manually from a keyboard

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

listItem = [a,b,c]

print(listItem)

listItem.sort()

print("max number:",  listItem[-1])

print("Otehr way max number:",  max(listItem))

