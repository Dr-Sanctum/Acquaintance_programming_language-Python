# Задание 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
import random
list_ratio = []
degree = random.randint(2, 5) #к=2...5
result = ''
for i in range(degree + 1):
    list_ratio.append(random.randint(0, 100))

for i in range(degree, 0, -1):
    if list_ratio[i] == 0: #Для пропуска нулевых коэфициентов x
        continue
    result = result + str(list_ratio[i]) + 'x^' + str(i) + '+'
if list_ratio[0] !=0:
    result = result + str(list_ratio[0]) + '=0'
elif list_ratio[0] ==0:
    result = result  + '=0'
    result = result.replace('+=0', '') #для удаления лишнего плюса при отсутствии последнего коэфициента
    result = result  + '=0'
result = result.replace('^1', '') #для удаления первой степени
# print(degree)
# print(list_ratio)
print(result)
with open('text1.txt', 'w+') as data:
    data.write(result)