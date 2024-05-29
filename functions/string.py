# uppercase
string = "Hi hema"
uppercase_string = string.upper()
print(uppercase_string)

# lowercase

string = "Hi Chaitu"
lowercase_string = string.lower()
print(lowercase_string)

# title 
string = "hi hemachaitanya"
title_string = string.title()
print(title_string)

# compare strings

string1 = "hi hemachaitanya"
string2 = "hi hema"
if string1 == string2:
    print("strings are equal")
else:
    print("strings are not equal")
    
# reverse order

name = 'hema'
print(name[::2])
print (name[1::2])
print (name[::4])
print (name[::3])
print (name[::-1])  # reverse order

# print msg

name = "hemachaitanya"

"hello, {name}".format(name="hemachaitanya")

## 

# value = "1-3b"
# if value.isnumeric():
#     print("{value}" "is numeric")
# elif value.isdecimal():
#     print("{value}" is decimal)
# elif value.alnum():
#     print(f"{value}" is alphanumeric)
# else:
#     print(f"{value}" "is float")

value = "1.25"
if value.isdecimal():
    print("{value}" "is decimal")
elif value.isnumeric():
    print("{value}" "is numeric")
else:
    print(f"{value}" "is float") # Without using an f-string, you would have to concatenate the string with the variable value using the + operator or use string formatting methods like % or .format(). F-strings provide a more concise and readable alternative.
    
    
## colours

colors = ["black", "yellow", "green", "red", "blue"]
fav_colors = ",".join(colors)
print(fav_colors)

## stripping

name = "    hema  "
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())

## partitions

word = " aws is first cloud"
result = word.partition('is')
print(result)
result = word.partition('first')
print(result)

## lines

statement = """ hello hema
how are you
things are great"""
print(statement)
lines = statement.split('\n')
word_count = len(lines)
print(lines)
for line in lines:
    words = line.split(' ')
    print (f"words sre {words}")
    word_count += len(words)
    print(f"word count is {word_count}")

## print path

# path = "C:\Users\batchu sivaji\hemalatha\python\for.py"
# print(path)


## escape sequences in python

path = r"C:\Users\batchu sivaji\hemalatha"
print(path)


##
path = "C:\\Users\\batchu sivaji\\hemalatha\\python\\for.py"
print(path)

## 

message = "Hello hema how \'re you"
print(message)

## 