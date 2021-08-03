# 9. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

three_nums = list(map(float, input('Введите три разных числа через пробел: ').strip().split()))
if (len(set(three_nums))) != 3:
    raise ValueError('Три числа!')
three_nums.sort()
print(three_nums[1])
