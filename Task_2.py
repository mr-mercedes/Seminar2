# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(number: int):
    sum = 1
    for i in range (1, number + 1):
        sum *= i
        print(sum, end=' ')

user_number = int(input('Введите число: '))
factorial(user_number)