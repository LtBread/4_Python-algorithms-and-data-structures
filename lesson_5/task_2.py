"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
 каждое число представляется как массив, элементы которого это цифры числа. Например,
  пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
   Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

   """

ELS_HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


class Hexadecimal:
    def __init__(self, hex_list):
        self.hex_list = hex_list

    def __str__(self):
        return f'{self.hex_list}'

    def __add__(self, other):
        _result = int(''.join(self.hex_list), 16) + int(''.join(other.hex_list), 16)
        result = list(str(hex(_result)).upper())[2:]
        return self.__class__(result)

    def __mul__(self, other):
        _result = int(''.join(self.hex_list), 16) * int(''.join(other.hex_list), 16)
        result = list(str(hex(_result)).upper())[2:]
        return self.__class__(result)


def hex_check(value):
    for el in value:
        if el not in ELS_HEX:
            raise ValueError('То, что вы ввели не является шестнадцатеричным числом!')
    return value


l_hex = Hexadecimal(hex_check(list(input('Введите левый операнд: ').strip().upper())))
r_hex = Hexadecimal(hex_check(list(input('Введите правый операнд: ').strip().upper())))
print(l_hex, r_hex)
print(l_hex + r_hex)
print(l_hex * r_hex)
