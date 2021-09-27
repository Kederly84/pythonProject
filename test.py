ask_number = 45
user_answer = int(input('Введи загаданное число: '))

if user_answer == ask_number:
    print('Маладец! Угадал')
elif user_answer < ask_number:
    print('Малавата будет')
else:
    print('эка ты маханул')
