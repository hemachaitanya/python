## 18th class room notes


print("hemalatha")

# to run this pyhton in terminal using 
# python <filename>

sum = 0
for index in range(1,10):
    if index%4 == 0 or index%7 == 0:
        sum = sum + index
print(sum)

## for 1 to 100

sum = 0
for index in range(1,101):
    if index%4 == 0 or index%7 == 0:
        sum = sum + index
print(sum)

## print 10 numbers

while index<10:
    sum = sum +10
print(sum)


### even or odd number 
number = 10
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
