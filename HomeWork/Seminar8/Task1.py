"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

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


m1 = Matrix([[4,6,2,],[5,8,5],[6,0,1]])
m2 = Matrix([[6,1,3],[4,6,9],[3,5,4]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)