"""3. Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Результат анализа работы скрипта task_2_3.py
Скопировано из консоли:

Введите натуральное число: 1
Обратное:  1
7       # результат вызова print(sys.getrefcount(number))
2       # результат вызова print(sys.getrefcount(rebmun))

Введите натуральное число: 999
Обратное:  999
2       # результат вызова print(sys.getrefcount(number))
2       # результат вызова print(sys.getrefcount(rebmun))

print(sys.getrefcount(number))  результат меняется в зависимости от введённого числа
встречались результаты: 2, 7, 9
print(sys.getrefcount(rebmun))  результат всегда 2

"""
import sys

number = input("Введите натуральное число: ")
rebmun = number[::-1]  # rebmun - это number наоборот
if not rebmun.isdigit():
    raise ValueError('Вы ввели не натуральное число, а что-то другое!')
print('Обратное: ', rebmun)
print(sys.getrefcount(number))
print(sys.getrefcount(rebmun))
