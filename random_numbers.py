# number guessing user with is 6 chances

import random
Number =  random.randint(1,50)
# print(Number)
for chance in range(1 ,7): # 6 attempts to find number thats way we give 1-7(6,0,-1)
    guessed_number = int(input("enter the number:"))
    if guessed_number == Number:
        print("your number is correct")
        break
    elif guessed_number > Number:
        print("your number is too high")
    else:
        print("your number is too low")
if not did_user_win:
    print("bad luck")
    
