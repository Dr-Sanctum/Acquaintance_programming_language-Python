#//Задание: Найти кубы чисел от 1 до N

n = int(input('Введите ограничение выводимых кубов чисел '))
i = 1
while i <= n:
    print(f'{i**3} ')
    i+=1

# С использованием list comprehension

reuslt = [i**3 for i in range(1, n+1)]
print(reuslt)