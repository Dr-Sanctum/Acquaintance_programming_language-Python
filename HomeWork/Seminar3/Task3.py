# Задание 3 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list_number = [3.234, 1.62, 2.2787, 4.73, 6.7, 9.05, 6.72, 7.22, 8.4, 3.672, 1.1]

list_number_remains = []

for i in range(0, len(list_number)):
    list_number_remains.append(round(list_number[i] % 1, 10))
min_remains = min(list_number_remains)
max_remains = max(list_number_remains)
print(f'Минимальная дробная часть {min_remains}')
print(f'Максимальная дробная часть {max_remains}')
print(f'Разница между максимальным и минимальным значением дробной части элементов = {round(max_remains - min_remains, 10)}')