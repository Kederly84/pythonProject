numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))

winners = ['Max', 'Kate', 'Leo']

# Простой перебор
for winner in winners:
    print(winner)

# Перебор с range
for i in range(len(winners)):
    #print(i)
    print(i+1, ')', winners[i])

# вывести нечетные цифры
print(list(range(1, 100, 2)))
for number in range(1, 100, 2):
    print(number)
