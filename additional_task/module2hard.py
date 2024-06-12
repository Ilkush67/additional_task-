import random
def password():
    print('Первое поле выбирается случайным образом:')
    digit_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers_1 = random.choice(digit_1)
    digit_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in digit_2:
        for j in digit_2:
            if numbers_1 % (i + j) == 0:
                print(numbers_1, '=', i, '+', j)

    return numbers_1

password()


def password():
    print('Первое поле необходимо ввести самостоятельно:')
    numbers_1 = int(input('Введите число от 3 до 20 - '))
    digit_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in digit_2:
        for j in digit_2:
            if numbers_1 % (i + j) == 0:
                print(numbers_1, '=', i, '+', j)

    return numbers_1

password()