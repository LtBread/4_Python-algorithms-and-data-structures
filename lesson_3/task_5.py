"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

"""
numbers = [0, 8, -4, 5, -1, -3]
negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)
result = max(negative_numbers)
print(f'numbers[{numbers.index(result)}] = {result}')
