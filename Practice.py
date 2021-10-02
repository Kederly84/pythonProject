# создать уникальный список из элементов list 1 и list 2

my_list_1 = [2, 5, 8, 2, 2, 2, 2, 12, 12, 4, 8, 5, 5]
my_list_2 = [2, 7, 12, 3]
# НЕВЕРНОЕ РЕШЕНИЕ!!!!
# Если список состоит из повторяющихся значений они так же будут удалены!!!
# my_list_1 = set(my_list_1)
# my_list_2 = set(my_list_2)
# uniqe_my_list = list(my_list_1 - my_list_2)
# print(uniqe_my_list)

# Правильное решение
for number in my_list_1[:]: # ВАЖНО СОЗДАТЬ КОПИЮ СПИСКА ЧТОБЫ ИДУЩИЕ ПОДРЯД ЭЛЕМЕНТЫ ТАК ЖЕ ПРОВЕРЯЛИСЬ!!!!!
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)



# удалить дубликаты в list 1
unique_my_list_1 = list(set(my_list_1))
print(unique_my_list_1)

# вывод только не повторяющихся элементов
u_result = []

for a in my_list_1:
    if my_list_1.count(a) == 1:
        u_result.append(a)
print(u_result)


# вывести дату в текстовом формате
date = '02.10.2021'
d, m, y = date.split('.')
print(d, m, y)

months = {
    '01': 'январь',
    '02': 'февраль',
    '03': 'март',
    '04': 'апрель',
    '10': 'октября'
}
days = {
    '01': 'первое',
    '02': 'второе'
}
result = f'{days[d]} {months[m]} {y} года'
print(result)