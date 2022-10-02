# Задание 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
list_number = [3, 1, 2, 4, 6, 9, 6, 7, 8, 3, 1]

result = []
size_result = math.ceil(len(list_number)/2)
for i in range(0, size_result):
    result.append(list_number[i] * list_number[len(list_number) - 1 - i])
print(f'Сумма пар позиций с учётом центральной позиции для нечётного количества {result}')
