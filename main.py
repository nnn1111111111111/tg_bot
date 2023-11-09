import random
HELP = """/help - посмотреть доступные команды
   /add - добавить новую задачу
   /show посмотреть добавленные задачи"""
taskc = {

}
def add_task (date, task):
    if date in taskc:
        taskc[date].append(task)
    else:
        taskc[date] = []
        taskc[date].append(task)
    print("Ваша задача", task, " добавлена на дату", date)

run = True
randoms = ["drink a beer", "drink tea", "eat ice", "read book"]
while run:
    command = input("Введите команду: ")
    print(command)
    # команда помочь
    if command == "help":
        print(HELP)
    # Команда добавить задачу
    elif command == "add":
        date = input("Когда вам нужно выполнить задачу: ")
        task = input("Введите название задачи: ")
        add_task(date, task)
    # Команда посмотреть задачу
    elif command == "show":
        date = input("Введите дату: ")
        if date in taskc:
            for task in taskc[date]:
                print('- ', task)
        else:
            print("Такой даты нет!")
            break
    # Проверка названия команд
    elif command != "help" and command != "add" and command != "show" and command != "exit" and command != "randoms":
        print("Такой команды не существует")
        print(HELP)
    elif command == "randoms":
        task = random.choice(randoms)
        add_task("Сегодня", task)
    # Конец цикла
    else:
        command = "exit"
        break
print("Спасибо за использование! До свидания!")
