try:

    num = input("Введите число: ")

    num = int(num)
    
    num = 10 / num 

except ValueError:
    print("Ошибка: ValueError")
    
except ZeroDivisionError:
    print("Ошибка: ZeroDivisionError")
    
finally:
    print("Программа завершена")