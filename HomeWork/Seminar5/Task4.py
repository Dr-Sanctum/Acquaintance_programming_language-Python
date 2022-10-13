# Задание 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

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


def rle_decode(data: str):
    result_decode = ''

    for char in data:
        if char.isdigit():  # если символ цифра то пишем в счётчик
            counter = int(char)
        else:
            # если символ не цифра записываем в результат в количестве счётчика
            result_decode += char * counter
    return result_decode


with open('data.txt', 'w+') as data:
    data.write('AAAGGGQQQQDUWWWWWWWWOOOFFFFFFFFF')

with open('data.txt', 'r') as d:  # Читаем строку из файла
    data = d.read()
print(f'Исходные данные - {data}')

data_encode = rle_encode(data)  # Сжимаем данные и записываем в файл
print(f'Сжатые данные - {data_encode}')
with open('data_encode.txt', 'w+') as data:
    data.write(data_encode)

# Восстанавливаем данные и записываем в файл
data_decode = rle_decode(data_encode)
print(f'Восстановленные данные - {data_decode}')
with open('data_decode.txt', 'w+') as data:
    data.write(data_decode)
