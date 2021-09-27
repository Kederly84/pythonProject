
age = int(input('введите свой возраст '))
weight = int(input('введите свой вес '))

if age <= 30:
    if 50 < weight < 120:
        print('Вы в порядке')
    else:
        print('С вами что то не так')
elif 30 < age <= 40:
    if 50 < weight < 120:
        print('Вы в порядке')
    else:
        print('займись собой')
elif age > 40:
    if 50 < weight < 120:
        print('Вы в порядке')
    else:
        print('Сходи ко врачу')
else:
    print('Мы не знаем что с вами')

