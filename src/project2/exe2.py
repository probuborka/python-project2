def get_user_data():
    """Функция для получения данных от пользователя"""
    name = input("Имя? ")
    age = int(input("Возраст? "))
    return name, age

class AgeCalc:
    def __init__(self, name, age):
        """Инициализирует объект"""
        self.name = name
        self.age = age
        self.age_new = 0

    def calculate_age(self):
        """Метод для вычисления возраста через 5 лет"""
        self.age_new = self.age + 5

name, age = get_user_data()

calc = AgeCalc(name, age)
calc.calculate_age()

print(f"Привет, {calc.name}, через 5 лет тебе будет {calc.age_new}.")