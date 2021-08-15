"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
части: в одной находятся элементы, которые не меньше медианы, в другой – не больше
медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках

"""
import random


def get_median(sub, pivot_fn=random.choice):
    if len(sub) % 2 == 1:
        return subpart(sub, len(sub) / 2, pivot_fn)
    else:
        return 0.5 * (subpart(sub, len(sub) / 2 - 1, pivot_fn) +
                      subpart(sub, len(sub) / 2, pivot_fn))


def subpart(sub, k, pivot_fn):
    pivot = pivot_fn(sub)
    lows = [el for el in sub if el < pivot]
    highs = [el for el in sub if el > pivot]
    pivots = [el for el in sub if el == pivot]
    if k < len(lows):
        return subpart(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return subpart(highs, k - len(lows) - len(pivots), pivot_fn)


m = 3
array = [round(50 * random.random(), 2) for _ in range(2 * m + 1)]
print(*array)
print(get_median(array))
