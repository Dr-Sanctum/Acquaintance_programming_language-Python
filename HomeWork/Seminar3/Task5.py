# Задание 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число '))
posfibo = [0, 1]
for i in range(2, number+1):
    posfibo.append((posfibo[i-2]) + (posfibo[i-1]))
negfibo = []
for i in range(1, number+1):
    negfibo.insert(0, posfibo[i]*(-1)**(i+1))

print(negfibo+posfibo)
