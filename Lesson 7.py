# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
# print(cities)
# print(type(cities))
#
# cities = set(cities)
#
# print(cities)
# print(type(cities))
#
# cities ={'Las Vegas', 'Paris', 'Moscow'}
# cities.add('Birma') # добавление элемента в множество
# cities.add('Moscow') # повторяющийся элемент не добавиться
# print(cities)
#
# cities.remove('Moscow') # удаление элемента
# print(cities)
# print(len(cities)) # длина множества
#
# print('Paris' in cities) # проверка наличия элемента в множестве True/False
#
# for city in cities: # перебор элементов множества. Тип получемого элемента всегда str
#     print(city)
#     print(type(city))

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонт', 'Помада'}

# Объединение множеств. При объединении совпадающие элементы удаляются,остаются только уникальные.
print(max_things | kate_things)
# Определение повторяющихся элементов
print(max_things & kate_things)
# Определение уникальных элементов множества, относительно другого множества
# Первым идет множество уникальные элементы которого ммы определяем
print(max_things - kate_things)




