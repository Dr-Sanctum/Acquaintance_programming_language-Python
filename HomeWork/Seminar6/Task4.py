# Задание: Дан список строк , установить верхний регистр у  всех строк больше 3х символов
list_input = ['234sdfg','se','DSGSg','asdg','ed','qds',]

for i in range(len(list_input)):
    if len(list_input[i]) >= 3:
        list_input[i] = list_input[i].upper()

print(list_input)

# С использованием  map и lambda

list_result = list(map(lambda x: x if len(x)<= 3 else x.upper(), list_input))

print(list_result)