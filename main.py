# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# Попробуйте сделать задачу через свой алгоритм и через метод .count(). Оцените скорость работы.

import random
import time

start = time.perf_counter()

n = int(input("Введите натуральное число – количество элементов: "))
list_of_numbers = [random.randint(0, 100) for _ in range(int(n))]
# list_of_numbers = [int(input('')) for _ in range(int(n))]
print(list_of_numbers)
x = int(input("Укажите искомое число: "))
count = 0
for i in list_of_numbers:
    if i == x:
        count += 1
print(f"Число {x} встречается {count} раз-(а)")

end = time.perf_counter()
print(end - start)

# # Попробуйте сделать задачу через свой алгоритм и через метод .count(). Оцените скорость работы.

import random
import time

start = time.perf_counter()

n = int(input("Введите натуральное число – количество элементов: "))
list_of_numbers = [random.randint(0, 100) for _ in range(int(n))]
# list_of_numbers = [int(input('')) for _ in range(int(n))]
print(list_of_numbers)
x = int(input("Укажите искомое число: "))
count = list_of_numbers.count(x)
print(f"Число {x} встречается {count} раз-(а)")

end = time.perf_counter()
print(end - start)

# Я разницу по времени не увидел большую, может маленький диапазон чисел?
# И генерировал рандомно и прописывал искомое число и список сразу.. но с count запись явно лаконичнее и нет циклов

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
#  к заданному числу X. Пользователь в первой строке вводит
#  натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import math

n = int(input("Введите натуральное число : "))
list_num = list(range(1, n + 1))
x = int(input("Введите число : "))
print(list_num)
min = list_num[0]
for i in range(len(list_num) - 1):
    if x > len(list_num):
        print(n)
        break
    elif abs(x - list_num[i + 1]) < abs(x - min):
        min = list_num[i]
    elif x < list_num[0]:
        print(list_num[0])
        break
    else:
        print(min)
        break
