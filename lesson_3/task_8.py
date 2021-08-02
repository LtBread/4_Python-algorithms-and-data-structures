"""8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
элементов строк. Программа должна вычислять сумму введенных элементов
каждой строки и записывать ее в последнюю ячейку строки. В конце следует
вывести полученную матрицу.

"""


def show_matrix(matrix):
    for row in matrix:
        print(*row, sep='\t')


usr_mtx = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
show_matrix(usr_mtx)
for row in usr_mtx:
    row.append(sum(row))
print()
show_matrix(usr_mtx)
