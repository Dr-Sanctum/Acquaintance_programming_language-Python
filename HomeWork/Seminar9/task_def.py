from random import randint
import prime_numbers as pn
# Первая функция
def candy_bot(total_candy: int, max_candy_round: int):
    if total_candy > max_candy_round:
        return randint(1, max_candy_round)
    else:
        return total_candy
# Вторая функция
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
# Третья функция
def rle_encode(data: str):
    result_encoding = ''
    char = ''
    counter = 0
    for i in data:
        if char != i:
            # Для второй итерации и последующих при нахождении конца линейки символов
            # записываем то что запомнили и сбрасываем счётчик
            if counter != 0:
                result_encoding = result_encoding + str(counter) + char
                char = i
                counter = 1
            else:  # Для первого входа в цикл, просто запоминаем сивол и устанавливаем счётчик
                char = i
                counter = 1
        else:
            counter += 1  # Если линейка одинаковых символов продолжается то увеличиваем счётчик

    # добавление последних элементов которые нельзя отсеч обнаружением нового
    result_encoding = result_encoding + str(counter) + char
    return result_encoding

# Четвёртая функция
def rle_decode(data: str):
    result_decode = ''

    for char in data:
        if char.isdigit():  # если символ цифра то пишем в счётчик
            counter = int(char)
        else:
            # если символ не цифра записываем в результат в количестве счётчика
            result_decode += char * counter
    return result_decode

# Пятая функция
def prime_multipliers_number(number):  
    list_prime_number = pn.prime_numbers(number)
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

# Шестая функция
def view_uniq_elem_list(string_number):
    list_number = string_number.split(' ')
    list_number_len = len(list_number)
    counter_i = 0
    while counter_i < list_number_len:
        counter_j = counter_i + 1
        while list_number.count(list_number[counter_i]) > 1:
            if list_number[counter_i] == list_number[counter_j]:
                list_number.pop(counter_j)
                list_number_len -= 1
            else:
                counter_j += 1
        counter_i += 1
    return list_number

# 7-8 функции
class Matrix:
    def __init__(self, matrix:list[list]):
        self.my_matrix = matrix

    def __str__(self):
        return_str = ''
        for i in self.my_matrix:
            for j in i:
                return_str += f'{str(j)} ' 
            return_str += '\n'
        return return_str

    def __add__(self, other):
        matrix_result = [[]]

        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[i])):
                matrix_result[i].append(None)
                matrix_result[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
            if len(matrix_result) == len(self.my_matrix):
                break
            matrix_result.append([])
        return Matrix(matrix_result)

#Остальные 
class Cell:

    def __init__(self, size: int):
        self.quantity = '*' * size

    def make_order(self, size_row):
        result = ''
        counter = 0
        for i in self.quantity:
            result = result + i
            counter += 1
            if counter == size_row:
                result = result + '\n'
                counter = 0
        return result

    def __add__(self, other):
        return Cell(len(self.quantity) + len(other.quantity))

    def __sub__(self, other):
        if len(self.quantity) >= len(other.quantity):
            return Cell(len(self.quantity) - len(other.quantity))
        else:
            print('Клетка не может быть меньше нуля')
            exit()

    def __mul__(self, other):
        return Cell(len(self.quantity) * len(other.quantity))

    def __truediv__(self, other):
        return Cell(len(self.quantity) // len(other.quantity))

