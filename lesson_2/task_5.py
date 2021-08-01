"""5. Вывести на экран коды и символы таблицы ASCII, начиная с
символа под номером 32 и заканчивая 127-м включительно. Вывод
выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

"""

# 127 - управляющий символ удаления (Delete). Знака нет.

try:
    char_gen = ((num, chr(num)) for num in range(32, 128))
    while char_gen:
        for _ in range(10):
            alikey, alivalue = next(char_gen)
            print(f'{alikey}: {alivalue}', end='\t')
        print()
except StopIteration as e:
    print(e)
