def check_number():

    num = input("Введите число: ")

    if num == "":
        num = None
    
    if num is None:
        print("Ошибка: Пусто")
        return
    
    try:
        num = int(num)
    except ValueError: 
        print("Ошибка: не число")
        return
   
    if 10 <= num <= 20:
        print(f"Число {num} входит в диапазон [10, 20]")
    else:
        print(f"Число {num} не входит в диапазон [10, 20]")

check_number()