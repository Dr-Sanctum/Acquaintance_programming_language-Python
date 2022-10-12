# Задание 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def Rle_encode(data:str):
    result_encoding = ''
    char = ''
    counter = 0
    for i in data:
        if char != i:
            if counter != 0:
                result_encoding = result_encoding + str(counter)+ char
                char = i
                counter = 1
            else:
                char = i
                counter = 1
        else:
            counter +=1
    result_encoding = result_encoding + str(counter)+ char #добавление последних элементов которые нельзя отсеч обнаружением нового
    return result_encoding

def Rle_decode(data:str):
    result_decode = ''
    
    for char in data:
        if char.isdigit():
            counter = int(char)
        else:
            result_decode += char * counter
    return result_decode

with open('data.txt','w+') as data:
    data.write('AAAGGGQQQQDUWWWWWWWWOOOFFFFFFFFF')

with open('data.txt','r') as d:
    data = d.read()

print(f'Исходные данные - {data}')

data_encode = Rle_encode(data)
print(f'Сжатые данные - {data_encode}')

with open('data_encode.txt','w+') as data:
    data.write(data_encode)

data_decode = Rle_decode(data_encode)
print(f'Восстановленные данные - {data_decode}')

with open('data_decode.txt','w+') as data:
    data.write(data_decode)