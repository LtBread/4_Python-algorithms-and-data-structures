"""1. Написать программу, которая будет складывать, вычитать, умножать или
делить два числа. Числа и знак операции вводятся пользователем. После
выполнения вычисления программа не должна завершаться, а должна запрашивать
новые данные для вычислений. Завершение программы должно выполняться при
вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю
о невозможности деления на ноль, если он ввел 0 в качестве делителя.

"""
import re
import numpy


def round_hand(num, n=4):  # Списал с урока
    return round(num, -int(numpy.log10(num) + 2 - n))


def row_parse(row):  # возвращает словарь
    pattern = re.compile(
        r'([-]*\d+(?:[.]\d+)*)'
        r'([+*/0-])'
        r'(\d+(?:[.]\d+)*)')
    result = pattern.match(row)
    if not result:
        raise ValueError(f'Вы не то что-то ввели: {row}')
    return result.groups()


while 1:
    print('0, +, -, *, /')
    try:
        user_row = input("Введите операцию. Например 2+2. Для выхода "
                         "введите '0' в качестве знака операции: "
                         "").replace(' ', '')
        l_oprnd, sign, r_oprnd = row_parse(user_row)
        l_oprnd = float(l_oprnd)
        r_oprnd = float(r_oprnd)
        if sign == '+':
            print(f'{l_oprnd} + {r_oprnd} = {round_hand(l_oprnd + r_oprnd)}')
        elif sign == '-':
            print(f'{l_oprnd} - {r_oprnd} = {round_hand(l_oprnd - r_oprnd)}')
        elif sign == '*':
            print(f'{l_oprnd} * {r_oprnd} = {round_hand(l_oprnd * r_oprnd)}')
        elif sign == '/':
            print(f'{l_oprnd} / {r_oprnd} = {round_hand(l_oprnd / r_oprnd)}')
        elif sign == '0':
            print('Выход')
            break
    except ValueError as e:
        print(e)
