# Задание 1 Вычислить число π c заданной точностью d
import math
accuracy_string = input('Введите точность вывода числа π в в виде 0.0...1 - ')
pi_string = str(math.pi)
pi_accuracy = float(pi_string[0:len(accuracy_string)])
print(pi_accuracy)