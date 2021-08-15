"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).

"""
import random
import sys
import time


def bubble_sort(sub):
    """
    Алгоритм оптимизирован.
    :param sub:
    :return: sub
    """
    sort_sub_cnt = 1
    while sort_sub_cnt < len(sub):
        check = False
        for i in range(len(sub) - sort_sub_cnt):
            if sub[i] < sub[i + 1]:
                sub[i], sub[i + 1] = sub[i + 1], sub[i]
                check = True
        sort_sub_cnt += 1
        if not check:
            break


dimension = 100
array = [random.randint(-100, 100) for _ in range(dimension)]
print('Первичный список:')
print(*array)
start = time.perf_counter()
bubble_sort(array)
stop = time.perf_counter() - start
print('Отсортированный список:')
print(*array)
print()
print(f'Время выполнения сортировки: {stop}')
print(f'Занимаемая память: {sys.getsizeof(array)} б')
