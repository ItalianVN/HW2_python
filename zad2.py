# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = input('ВВедите вещественное число: ') 
my_fact = 1
if str.isnumeric(num) == True:
    for i in range(1,int(num)+1):
        my_fact = my_fact*i
        print(my_fact, end=' ')
else:
    print('число не вещественное')











