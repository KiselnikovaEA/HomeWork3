# Задача 1: Программа найдёт сумму элементов списка, стоящих на нечётной позиции

# def sum_of_odd_elements(some_array):
#     sum = 0
#     for i in range(1, len(some_array), 2):
#         sum = sum + some_array[i]
#     return sum

# some_array = [2, 3, 5, 9, 3, 7, 12, 6]
# print(sum_of_odd_elements(some_array))


# Задача 2: Программа найдёт произведение пар чисел списка. Парой считается первый и последний элемент, второй и предпоследний и т.д.

# def mult_couple_numbers(some_array):
#     mult_array = []
#     if(len(some_array) % 2 == 1):
#         for i in range(0, int(len(some_array)/2)+1):
#             mult_array.append(some_array[i] * some_array[len(some_array) - i - 1])

#     else:
#          for i in range(0, int(len(some_array)/2)):
#             mult_array.append(some_array[i] * some_array[len(some_array) - i - 1])
#     return mult_array

# #some_array = [2, 3, 4, 5, 6]
# some_array = [2, 3, 4, 5]
# print(mult_couple_numbers(some_array))


# Задача 3: Программа найдёт разницу между максимальным и минимальным значением дробной части элементов списка из вещественных чисел

# def magic_function(some_array):
#     some_array_2 = []
#     for i in range(0, len(some_array)):
#         h = int(some_array[i])
#         some_array_2.append(round(some_array[i] - h, 2))
#     h = max(some_array_2) - min(some_array_2)
#     return h



# some_array = [1.1, 1.2, 3.1, 5, 10.01]
# print(magic_function(some_array))


# Задача 4: Программа будет преобразовывать десятичное число в двоичное

# def int_to_binary(num):

#     some_array = []
#     i = 0
#     while num != 1:
#         some_array.append(num % 2)
#         num = int(num / 2)
#         i = i + 1

#     some_array.append(1)
#     some_array.reverse()
#     print(*some_array, sep='')

# num = int(input('Введите число: '))
# int_to_binary(num)


# Задача 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def negafib(k):
#     fib_array = []
#     fib_array.append(0)
#     fib_array.append(1)
#     for i in range(1, k):
#         fib_array.append(fib_array[i] + fib_array[i - 1])
#     for _ in range(1, k + 1):
#         fib_array.insert(0, fib_array[1]-fib_array[0])
#     return fib_array


# k = int(input('Введите число k: '))
# print(*negafib(k), sep=' ')