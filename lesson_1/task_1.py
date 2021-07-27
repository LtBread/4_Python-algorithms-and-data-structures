# 1. Найти сумму и произведение цифр трехзначного числа,
#  которое вводит пользователь.


def saw_through(num):
    saw_cut = []
    while num != 0:
        saw_cut.append(num % 10)
        num = num // 10
    return saw_cut


def mult(nums):
    result = 1
    for el in nums:
        result *= el
    return result


user_numb = int(input('Введите натуральное трёхзначное число: '))
if not (99 < user_numb < 1000):
    raise ValueError('То, что вы ввели - не трёхзначное число!')
sum_result = sum(saw_through(user_numb))
mult_result = mult(saw_through(user_numb))
print('Сумма цифр числа равна: ', sum_result)
print('Произведение цифр числа равно: ', mult_result)
