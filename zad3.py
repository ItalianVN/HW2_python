# 3 Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = input('Введите число: ')

if str.isnumeric(num) == True:
    num = int(num)
    def sequence(num):

        return[round((1 + 1 / n)**n, 2) for n in range (1, num + 1)]   
        
    print(sequence(num))
    print((sum(sequence(num))))
else:
    print('число не вещественное')


