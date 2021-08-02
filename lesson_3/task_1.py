"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из
них кратны каждому из чисел в диапазоне от 2 до 9.

"""
big_subsequence = [num for num in range(2, 100)]
little_subsequence = [num for num in range(2, 10)]
counter = 0
for little_num in little_subsequence:
    for big_num in big_subsequence:
        if not big_num % little_num:
            counter += 1
    print(f'Числу {little_num} кратны {counter} '
          f'числа (чисел) из диапазона 2 - 99')
    counter = 0
