# Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input('Введите целое число '))

result = []
for i in range(1, n + 1):
    temp = 1
    for j in range(1, i):
        temp += temp * j
    result.append(temp)
print(result)