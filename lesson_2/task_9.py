"""9. Среди натуральных чисел, которые были введены, найти наибольшее по
сумме цифр. Вывести на экран это число и сумму его цифр.

"""


def sum_saw_through(num):  # функция разбивает число и возвращает сумму его цифр
    saw_cut = []
    while num != 0:
        saw_cut.append(num % 10)
        num = num // 10
    return sum(saw_cut)


numbers = list(map(int, input(
    'Введите через запятую несколько натуральных чисел: ').replace('-', '').split(',')))
print(numbers)
dict_num = dict()
for number in numbers:
    dict_num[sum_saw_through(number)] = number
print(f'Наибольшее: {dict_num.get(max(dict_num.keys()))}: {max(dict_num.keys())}')
