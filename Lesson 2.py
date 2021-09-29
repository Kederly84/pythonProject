# friend = 'Александр'
#
# first_letter = friend[0]
#
# print('Первая буква ', first_letter)
# print('Тип значения работы индекса ', type(first_letter))
#
# print('Вторая буква ', friend[1])
# print('Первая буква с конца', friend[-1])
# print('Срез со второго по 4ый элемент ', friend[1:4])
# print('Срез со второго элемента до конца строки ', friend[1:])
# print('Срез с первого по 4ый элемент ', friend[:4])

# friends = 'Максим Леонид 123'
#
# print(friends)
# print(len(friends))
# print('Индекс искомого ', friends.find('Лео'))
# print('В данном случае преобразование строки в список с разделителем пробел ', friends.split())
# print('Проверка состоит ли строка из чисел ', friends.isdigit())
# print('Все буквы в верхний регистр ', friends.upper())
# print('Все буквы в нижний регистр ', friends.lower())

# name = 'Leo'
# age = 30

# Конкатенация
# hello_str = name + ' ' + str(age)
# print(hello_str)
# %
# hello_str = '%s %d'%(name, age) #%s -сюда идет строка (s - str) %d - сюда число (d - digital)
# print(hello_str)
# format
# hello_str = '{} {}'.format(name, age)
# print(hello_str)

top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов'
# Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом

start = top5.find('1')
end = top5.find('4')

top3 = top5[start:end]
result = 'Поздравляем {} с успехом'.format(top3.upper())

print(result)
