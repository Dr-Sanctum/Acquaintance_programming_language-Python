# Задание: Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
from functools import reduce
list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = 0
for i in range(1, len(list_number), 2):
    result += list_number[i]
print(f'Сумма нечётных позиций {result}')

# С использованием list comprehension, reduce и lambda

result = [i for i in list_number if i % 2]
result = reduce(lambda item, item2: item + item2, result)
print(f'Сумма нечётных позиций {result}')
