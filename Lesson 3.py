# Можно объявить пустой список

empty_list = []

# можно объявить заполненный список
friends = ['Leo', 'Max', 'Kate']

# Тип списка - list
# print(type(friends))

# Как и встроке для списка доступны индексы
# print('Первое имя ', friends[0])
# print('Первое имя с конца ', friends[-1])

# Так же можно применять срезы. Срезы обязательно вернуть список.
# print('Второе и третье имя ', friends[1:2])
# print('Второе и третье имя ', friends[1:])
# print('Первое и второе имя ', friends[:2])
# print('Длина списка', len(friends))
# friends.append('Ron') # добавление элемента в список
# print(friends)
#
# print(friends.pop()) # Удаляет последний элемент списка и возвращает его
# print(friends)
#
# friends.clear() # Очистка списка
# print(friends)
#
# friends = ['Leo', 'Max', 'Kate']
# friends.remove('Kate') # Удаление выбранного элемента из списка
# print(friends)
#
# del friends[1] # Удаление элемента по индексу
# print(friends)

hero = 'Superman'

if hero.find('man') != -1:
    print('Есть')
else:
    print('Нету')

if 'man' in hero:
    print('Есть')
else:
    print('Нету')

if 'Max' in friends:
    print('Есть')
else:
    print('Нету')