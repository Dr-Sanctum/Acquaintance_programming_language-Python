# Задание 5 Даны два файла, в каждом из которых находится запись многочлена,
# приравненного к нулю. Задача - сформировать файл, содержащий
# сумму многочленов (суммируем подобные слагаемые).
import Task4


Task4.equation_to_file('text1.txt', 3, 3)
Task4.equation_to_file('text2.txt', 3, 3)


with open('text1.txt', 'r') as data:
    string_text1 = str(*data)
with open('text2.txt', 'r') as data:
    string_text2 = str(*data)
string_text1 = string_text1.replace('=0', '')
string_text2 = string_text2.replace('=0', '')

equation_1 = string_text1.split('+')
equation_2 = string_text2.split('+')
len_result = max(1 if equation_1[0][-1] == 'x' else int(equation_1[0][-1]),
                 1 if equation_2[0][-1] == 'x' else int(equation_2[0][-1])) + 1
print(equation_1)
print(equation_2)
print(len_result)
print()
i = 0
while len(equation_1) < len_result:
    if equation_1[i][-1] != ' ' and equation_1[i][-1] != 'x' and len(equation_1[i]) == 1:
        equation_1.insert(i, ' ')
        i += 1
    elif equation_1[i][-1] != 'x' and int(equation_1[i][-1]) == len_result - i - 1:
        i += 1
        if i == len(equation_1) - 1 and len(equation_1[i]) != 1:
            while len(equation_1) < len_result:
                equation_1.append(' ')
                i += 1
        continue
    elif equation_1[i][-1] == 'x' and i != len_result - 2:
        equation_1.insert(i, ' ')
        i += 1
    elif equation_1[i][-1] != 'x' and int(equation_1[i][-1]) != len_result - i - 1:
        equation_1.insert(i, ' ')
        i += 1
        if i == len(equation_1) - 1 and len(equation_1[i]) != 1:
            equation_1.append(' ')
    elif equation_1[i][-1] != 'x' and i == len_result - 1:
        equation_1.insert(i, ' ')
        break
    elif equation_1[i][-1] == 'x':
        equation_1.append(' ')
    else:
        while len(equation_1) < len_result:
            i += 1

while len(equation_2) < len_result:
    if equation_2[i][-1] != ' ' and equation_2[i][-1] != 'x' and len(equation_2[i]) == 1:
        equation_2.insert(i, ' ')
        i += 1
    elif equation_2[i][-1] != 'x' and int(equation_2[i][-1]) == len_result - i - 1:
        i += 1
        if i == len(equation_2) - 1 and len(equation_2[i]) != 1:
            while len(equation_2) < len_result:
                equation_2.append(' ')
                i += 1
        continue
    elif equation_2[i][-1] == 'x' and i != len_result - 2:
        equation_2.insert(i, ' ')
        i += 1
    elif equation_2[i][-1] != 'x' and int(equation_2[i][-1]) != len_result - i - 1:
        equation_2.insert(i, ' ')
        i += 1
        if i == len(equation_2) - 1 and len(equation_2[i]) != 1:
            equation_2.append(' ')
    elif equation_2[i][-1] != 'x' and i == len_result - 1:
        equation_2.insert(i, ' ')
        break
    elif equation_2[i][-1] == 'x':
        equation_2.append(' ')
    else:
        while len(equation_2) < len_result:
            i += 1
print(equation_1)
print(equation_2)
print('')
result_equation = []
for i in range(len(equation_1)):
    if equation_1[i] != ' ' and equation_2[i] !=' ':
        if equation_1[i] == 'x' or equation_2[i] =='x':
            str_1  = 1 if equation_1[i][0] == 'x' else int(equation_1[i][0])
            str_2  = 1 if equation_2[i][0] == 'x' else int(equation_2[i][0])
            str_result = f'{str_1 + str_2} + x'
            result_equation.append(str_result)
        str_result = f'{str(int(equation_1[i][0]) + int(equation_2[i][0])) + equation_1[i][1:]}'
        result_equation.append(str_result)
    else:
        str_result = equation_1[i] + equation_2[i]
        str_result = str_result.replace(' ', '')
        result_equation.append(str_result)
for i in range(len(result_equation)-1):
    result_equation[i] = result_equation[i]+ '+'
print(result_equation)
string_result = ''.join(result_equation) + '=0'
print(string_result)
with open('text_result.txt', 'w+') as data:
    data.write(string_result)

