# 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = input('ВВедите вещественное число: ')
str_num = str(num)
str_num = str_num.replace('.', '')
str_num = str_num.replace(',', '')
str_num = str_num.replace('-', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
my_sum = sum(lst_num)
print(my_sum)


