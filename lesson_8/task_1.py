"""1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

"""
import hashlib


def substring_counter(string, *args):
    if not args:
        raise ValueError('Вы не задали подстроки, которые нужно искать!')
    counters = {substring: 0 for substring in args}
    for substring in args:
        len_sub = len(substring)
        h_subs = hashlib.sha1(substring.encode('utf-8')).hexdigest()
        for i in range(len(string) - len_sub + 1):
            if h_subs == hashlib.sha1(string[i:i + len_sub].encode('utf-8')).hexdigest():
                counters[substring] += 1
    return counters


given_string = 'afdsafnjklwefnjwfwbjkvshfbdlsf'
substring_1 = 'af'
substring_2 = 'ere'
print(substring_counter(given_string, substring_1, substring_2))
