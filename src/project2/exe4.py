import sys

def check_num(num:int):

    if num > 0:
        print("positive")
    elif num == 0:
        print("zero")
    else:
        print("negative")

    b2: bool = num % 2 == 0
    b3: bool = num % 3 == 0
    
    if b2 and b3:
        print("Yes")
    else:
        print("No")

try:
    num = int(input("Number: "))
except ValueError: 
    print("Ошибка: не число")
    sys.exit()

check_num(num)