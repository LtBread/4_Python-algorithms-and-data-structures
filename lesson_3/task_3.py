"""3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.

"""
numbers = [2, 6, 1, 16, 17, 88]
print(numbers)
idx_min = numbers.index(min(numbers))
idx_max = numbers.index(max(numbers))
numbers[idx_min], numbers[idx_max] = numbers[idx_max], numbers[idx_min]
print(numbers)
