# Задание 5  Задайте список из n чисел последовательности 
#〖(1+1/n)〗^n и выведите на экран их сумму.

number = int(input('Введите целое число '))

list_number = []

for i in range(1, number + 1):
    list_number.append((1 + 1 / i)**i)
print(f'Последовательность - {list_number}')

result = 0
for i in range(number):
    result += list_number[i]
print(f'Сумма последовательности = {result}')