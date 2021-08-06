"""1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Решение задачи № 1 к уроку № 3.
Текст задания:
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из
них кратны каждому из чисел в диапазоне от 2 до 9.

"""
import time

"""Реализация 0. 
Сложность: О(n**2)
Время выполнения: 7.024932146072388 секунд

"""
start_time = time.time()
BIG_DIMENSION = 100000
LITTLE_DIMENSION = 1000
big_subsequence = [num for num in range(2, BIG_DIMENSION)]
little_subsequence = [num for num in range(2, LITTLE_DIMENSION)]
counter = 0
for little_num in little_subsequence:
    for big_num in big_subsequence:
        if not big_num % little_num:
            counter += 1
    print(f'Числу {little_num} кратны {counter} '
          f'числа (чисел) из диапазона 2 - {BIG_DIMENSION}')
    counter = 0
print(f'{time.time() - start_time} секунд')
