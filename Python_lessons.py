# Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

number = int(input('Введи число '))
print(number + 2)

# Используя цикл, запрашивайте у пользователя число,
# пока оно не станет больше 0, но меньше 10.

while (number < 0 or number > 10):
    number = int(input('Введи число от 1 до 9'))

print(number ** 2)
print('Молодец')
