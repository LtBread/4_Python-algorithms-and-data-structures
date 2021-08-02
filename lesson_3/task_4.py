"""4. Определить, какое число в массиве встречается чаще всего.

"""
numbers = [1, 2, 3, 4, 1, 4, 1, 5, 2, 2, 2, 2, 2]
frequency_numbers = dict()
frozen_num = set(numbers)
for frozen_num in frozen_num:
    frequency_numbers[numbers.count(frozen_num)] = frozen_num
print(f'Число {frequency_numbers.get(max(frequency_numbers.keys()))} '
      f'встречается {max(frequency_numbers.keys())} раз, а это больше всего')
