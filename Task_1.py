# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


def sum_numbers(number):
    sum = 0
    for i in range(len(number)):
        if number[i].isdigit():
            sum += int(number[i])
    return sum


user_number = input('Введите число: ')
print(f'Сумма чисел в числе {user_number} ровна {sum_numbers(user_number)}')
