# Задание 4  Задайте число N, создайте список: [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции (случайные) хранятся в файле file.txt 
# (создаётся во время выполнения кода и зависит от количества элементов в списке) 
# в одной строке одно число.

import random

number = int(input('Введите целое число '))
list_number = []

for i in range( -number, number+1):
    list_number.append(i)
print(f'Последовательность - {list_number}')
# Создаём последовательность символов для записи в файл
filestring = []
for i in range(len(list_number)):
    filestring.append(str(random.randint(0, len(list_number)-1)))
file = open("file_task4", "w+")
try:
# Записывает построчно созданную последовательность индексов
    file.writelines("%s\n" % line for line in filestring)
finally:
    file.close

file = open("file_task4", "r")
try:
    filestring = file.readlines()
finally:
    file.close

# Перемножамем значения находящиеся на позициях извлечённых из файла
result = list_number[int(filestring[0])]

for i in range(1, len(filestring)-1):
    result = result * list_number[int(filestring[i])]

for i in range(0, len(filestring)-1):
    print(f'{filestring[i]}, {list_number[int(filestring[i])]}')
print(f'Результат = {result}')