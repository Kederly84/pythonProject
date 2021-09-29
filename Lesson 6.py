friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))

friend = friends[0]
print(friend)
print(type(friend))

# Добавить возраст человеку

friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))

print(friend['age'])

friend['Has car'] = True
print(friend)

friend['Has car'] = False
print(friend)

del friend['Has car']
print(friend)

if 'Has car' in friend:
    print('Есть машина')
else:
    print('Нет машины')

# Перебор по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

# Перебор по значениям
for val in friend.values():
    print(val)

# Перебор по паре ключ + значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)
