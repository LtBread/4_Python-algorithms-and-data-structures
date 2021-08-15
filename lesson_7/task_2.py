"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.

"""
import random
import sys
import time


def merger_sort(sub, start=0, end=None):
    def subpart(sub, start, end, pivot_index):
        sub[start], sub[pivot_index] = sub[pivot_index], sub[start]
        pivot = sub[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if sub[y] <= pivot:
                sub[y], sub[x] = sub[x], sub[y]
                x += 1
            y += 1

        sub[start], sub[x - 1] = sub[x - 1], sub[start]
        return x - 1

    if end is None:
        end = len(sub) - 1
    if end - start < 1:
        return

    pivot_index = (start + end) // 2
    x = subpart(sub, start, end, pivot_index)
    merger_sort(sub, start, x - 1)
    merger_sort(sub, x + 1, end)


dimension = 10000
array = [round(50 * random.random(), 2) for _ in range(dimension)]
print('Первичный список:')
print(*array)
start = time.perf_counter()
merger_sort(array)
stop = time.perf_counter() - start
print('Отсортированный список:')
print(*array)
print()
print(f'Время выполнения сортировки: {stop}')
print(f'Занимаемая память: {sys.getsizeof(array)} б')
