# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


def fill_array(number: int):
    new_array = []
    for i  in range(-number,number + 1):
        new_array.append(i)
    return new_array

def find_array(array, indexes):
    new_array = []
    count = 0
    for i  in range(len(array)):
        if count == len(file_txt):
            break
        elif i == file_txt[count] and count < file_txt[len(file_txt) - 1]:
            new_array.append(array[i])
            count += 1
    return new_array

def compose(array):
    sum_array = []
    for i in range(1, len(array), 2):
        sum_array.append(array[i] * array[i - 1])
    return sum_array
        
    
user_number = int(input('Введите число: '))
file_txt = [int(i) for i in input('Введите индексы элементов: ').split()]
array_nn = fill_array(user_number)
print(f'Начальный диапазон ---> {array_nn}')
compose_array = find_array(array_nn, file_txt)
print(f'Искомые элементы по индексам  ----> {compose_array}')
anser_array = compose(compose_array) 
print(f'Произведение элементов ---> {anser_array}')