"""4. Найти сумму n элементов следующего ряда чисел:
 1 -0.5 0.25 -0.125 ...
 Количество элементов (n) вводится с клавиатуры.

 """
n = int(input('введите натуральное число: '))
hoarder = 0
for el in range(n):
    if el % 2:
        hoarder += (-1 ** (el - 1)) / 2 ** el
    else:
        hoarder += (1 ** (el - 1)) / 2 ** el
print(hoarder)