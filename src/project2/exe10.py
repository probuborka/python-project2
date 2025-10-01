# 1
num = int(input("Введите число: "))
print(f"{"even" if num % 2 == 0 else "odd"}")

# 2
if (user_input := input("Введите строку: ")).isdigit():
    print("Это число")
else:
    print("Это не число")