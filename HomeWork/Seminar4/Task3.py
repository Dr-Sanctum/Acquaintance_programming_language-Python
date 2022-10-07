# Задание 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def view_uniq_elem_list (string_number):
    list_number = string_number.split(' ')
    print(list_number)
    list_number_len = len(list_number)
    counter_i = 0
    while counter_i < list_number_len:
        counter_j = counter_i + 1
        while list_number.count(list_number[counter_i]) > 1:
            if list_number[counter_i] == list_number[counter_j]:
                list_number.pop(counter_j)
                list_number_len -= 1
            else:
                counter_j+=1
        counter_i+=1
    print(list_number)

string_number = input('Введите последовательность чисел разделяя пробелом - ')
view_uniq_elem_list(string_number)