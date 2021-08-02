"""9. Найти максимальный элемент среди минимальных элементов столбцов
матрицы.

"""


def show_matrix(matrix):
    for row in matrix:
        print(*row, sep='\t')
    print()


usr_mtx = [
    [-1, -1, -9, 4],
    [5, 6, -7, 8],
    [9, 10, 0, -12],
    [13, 14, -15, 16]
]
show_matrix(usr_mtx)
usr_mtx_reverse = list(zip(*usr_mtx))  # транспонирование
show_matrix(usr_mtx_reverse)
min_of_row = []  # минимальные элементы по строкам в транс-ой м-це
for row in usr_mtx_reverse:
    min_of_row.append(min(row))
print(f'Максимальный элемент среди минимальных элементов столбцов'
      f'матрицы: {max(min_of_row)}')
