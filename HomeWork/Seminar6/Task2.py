# Задание Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
from functools import reduce

number = input('Введите вещественное число ')

numberResult = number.replace(',', '')
numberResult = number.replace('.', '')
result = 0
for i in range(len(numberResult)):
    result += int(numberResult[i])
print(f'Сумма цифр числа {number} = {result}')

# С использованием list comprehension, filter, reduce и lambda

result = list(filter(lambda x: x != ',' and x !='.', number))
result = reduce(lambda i, i2: int(i) + int(i2), result)
print(f'Сумма цифр числа {number} = {result}')
