"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

Для сравнения обе функции возвращают 999-е простое число
"""

import time

"""Самодельная функция нахождения i-го по счёту простого числа
Сложность: O(n**2)
Время выполнения: 0.16758131980895996 секунд

"""


def artisanal_func(required_position):
    """
    Нумерация простых чисел начинается с 1 (2 - простое число имеет номер 1)
    Функция принимает порядковый номер простого числа и возвращает это простое
    число
    :param required_position:
    :return: simple
    """
    if required_position <= 0:
        raise ValueError('Вы ввели ноль или того хуже!')
    simple = 2
    position_simple = 1
    verifiable_num = 2
    while position_simple <= required_position:
        for num in range(2, verifiable_num - 1):
            if not verifiable_num % num:
                break
        else:
            simple = verifiable_num
            position_simple += 1
        verifiable_num += 1
    return simple


"""Решето Эратосфена
Сложность: O(n*log(log n) Списал с Википедии
Время выполннения: 0.031946659088134766 секунд

"""


def sieve_eratosthenes(required_position, dimension):
    """
    Нумерация простых чисел начинается с 1 (2 - простое число имеет номер 1)
    Реализация алгоритма "Решето Эратосфена" для поиска простого числа по его
    номеру.
    :param required_position:
    :param dimension:
    :return: num
    """
    if required_position <= 0:
        raise ValueError('Вы ввели ноль или того хуже!')
    position_simple = 0
    subsequence = [num for num in range(0, dimension)]
    subsequence[1] = 0
    m = 2
    while m < dimension:
        if subsequence[m] != 0:
            j = m * 2
            while j < dimension:
                subsequence[j] = 0
                j = j + m
        m += 1
    for num in subsequence:
        if num != 0:
            position_simple += 1
        if position_simple == required_position:
            return num
    else:
        raise Exception('Запрошенное простое число за '
                        'пределами введенного диапазона, '
                        'в следующий раз введите верхнюю границу '
                        'диапазона побольше')


target_position = int(
    input('Введите порядковый номер простого числа, '
          'которое хотите получить (нумерация начинается с 1): '))
print('Без использования «Решета Эратосфена»')
start_time = time.time()
print(f'{target_position}-е по счёту простое число:'
      f' {artisanal_func(target_position)}')
print(f'{time.time() - start_time} секунд')
print('Используя алгоритм «Решето Эратосфена»')
target_dimension = int(
    input('Введите число, до которого решето сгенерирует последовательность,'
          'в которой находится искомое простое число: '))
start_time = time.time()
print(f'{target_position}-е по счёту простое число:'
      f' {sieve_eratosthenes(target_position, target_dimension)}')
print(f'{time.time() - start_time} секунд')
