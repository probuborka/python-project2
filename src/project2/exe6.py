def set_command(command):

    match command:
        case "start":
            return "Запуск"
        case "stop":
            return "Остановка"
        case "pause":
            return "Пауза"
        case _:
            return "Неизвестная команда"
        
command = input("Введите команду: ")
print(set_command(command))