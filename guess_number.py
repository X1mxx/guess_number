from random import randint

secret_number = randint(1, 100)
print('Угадайте число от 1 до 100')


while True:
    user_number = int(input('Введите число: '))

    if user_number < secret_number:
        print('Ваше число меньше загаданного, попробуйте ещё раз')
    elif user_number > secret_number:
        print('Ваше число больше загаданного, попробуйте ещё раз')
    else:
        print('Вы угадали! Загаданное число -', secret_number)
        break