# 5. Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят и сколько между ними находится букв.
"""
97 == 1
122 == 26
"""


def let_space(letter):
    if 97 <= ord(letter) <= 122:
        space = ord(letter) - 96
        return space
    raise ValueError('То, что вы ввели - не английские буквы')


letter_1, letter_2 = input(
    'Введите две разные английские буквы через пробел: ').strip().split()
if letter_1 == letter_2:
    raise ValueError('Вы ввели два одинаковых... что бы там ни было.')
print(f'Буква {letter_1} на {let_space(letter_1)} месте,'
      f'буква {letter_2} на {let_space(letter_2)} месте,'
      f'между ними {abs(let_space(letter_2) - let_space(letter_1)) - 1} букв(ы)')
