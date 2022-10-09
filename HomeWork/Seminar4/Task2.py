# Задание 2 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def prime_numbers(number_max:int):
    list_normal_number = list(range(2, number_max + 1))
    list_cheked = list_normal_number.copy()
    for i in list_cheked:
        counter_j = 0
        first = True
        while counter_j < len(list_normal_number):
            # print(list_normal_number)
            # print(i)
            # print(list_normal_number[counter_j])
            # print(first)
            if first == True and list_normal_number[counter_j] % i == 0:
                first = False
                counter_j += 1
                continue
            elif first == False and list_normal_number[counter_j] % i == 0:
                list_normal_number.pop(counter_j)
            counter_j += 1
    return list_normal_number
def prime_multipliers_number(number):  
    list_prime_number = prime_numbers(number)
    multipliers_number = []
    for i in list_prime_number:
        if number == i:
            multipliers_number.append(i)
            break
        elif number % i == 0:
            while number % i == 0:
                number = number / i
                multipliers_number.append(i)
    return multipliers_number

number = int(input('Введите число - '))
print(prime_multipliers_number(number))