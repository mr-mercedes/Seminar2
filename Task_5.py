# Реализуйте алгоритм перемешивания списка.

from random import shuffle

def fill_array(length):
    array = []
    for i in range(1, length + 1):
        array.append(i)
    return array


user_number = int(input('Введите длинну массива: '))
array = fill_array(user_number)
print(f'Начальный массив ----> {array} <-----')
shuffle(array)
print(f'Сортированный массив ----> {array} <-----')
