# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def mathematic(number: int):
    sum = 0
    for i in range(1, number + 1):
        sum = (1 + (1 / i))  ** i 
        print(sum, end=' ')
    

user_number = int(input('Введите число: '))
mathematic(user_number)