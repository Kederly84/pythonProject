# Пользователь вводит кол-во участников соревнований
# Пользователь указывает имена участников и место которое занял каждый участник
# 1. Вывод имен участников по алфавиту
# 2. Получить 3х победителей и поздравить их
# 3. Победители: ...... Поздравляем!

print('Соревнования по Python')

count = int(input('Введите кол-во участников '))

i = count
members = []

while i > 0:
    name = input('Кто занял {} место'.format(i))
    members.append(name)
    i -= 1

# Кто участвовал в соревнованиях (по алфавиту)
print('В соревновании участвовали ', sorted(members))

# Переворот списка
members.reverse()

# Берем первые 3 места
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
