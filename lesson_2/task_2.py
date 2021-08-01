"""2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
 и 2 нечетные (3 и 5).

"""


def show_count_odd_and_even(number):
    odd = 0
    even = 0
    if not number.isdigit() or number.startswith('0'):
        raise ValueError(f'wrong expression: {number}')
    for el in number:
        if int(el) % 2:
            odd += 1
        else:
            even += 1
    print(f'odd = {odd}, even = {even}')


try:
    user_number = input("enter the natural number: ").strip()
    show_count_odd_and_even(user_number)
except ValueError as e:
    print(e)
    exit(1)
