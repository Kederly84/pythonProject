# ИГРА "УГАДАЙ ЧИСЛО"
# №1 Программа загадывает число
import random

number = random.randint(1, 100)

# №2 и №3  ввод числа пользователя и реализация цикла проверки чисел
user_answer = None
counter = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности от 1 до 3'))
max_count = levels[level]

user_count = int(input('Введите кол-во пользователей: '))
users = []
is_winner = False
winner_name = ''

for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}')
    users.append(user_name)

while not is_winner:
    counter += 1
    if counter > max_count:
        print('Все игроки проиграли')
        break
    print(f'Попытка №: {counter}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_answer = int(input('Введи загаданное число: '))
        if user_answer == number:
            is_winner = True
            winner_name = user
            break
        elif user_answer > number:
            print('Вы загадали слишком большое число')
        else:
            print('Вы загадали слишком маленькое число')
else:
    print('Поздравляем вы победили. Загаданное число: ', number)