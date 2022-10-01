# Задание 1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

number = input('Введите вещественное число ')

numberResult = number.replace(',', '')
numberResult = number.replace('.', '')
result = 0
for i in range(len(numberResult)):
    result += int(numberResult[i])
print(f'Сумма цифр числа {number} = {result}')