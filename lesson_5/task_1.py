"""1. Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.

"""


def get_average(values):
    all_sum = 0
    for v in values:
        all_sum += sum(v)
    return all_sum / len(values)


enterprises = {
    'ООО "Рога и копыта': [1100000, 3240000, 12356200, 1200050],
    'ИП "Богадельня"': [5040000, 20100500, 9990006, 3150000],
    'ООО "Крошка-Окрошка"': [4000000, 4000000, 4000000, 4000000],
    'ОАО "Китайская надёжность"': [150000, 165000, 210000, 120000],
    'ИТДИТП "Синий Декабрь"': [40200500, 39050000, 3500002, 45000000],
    'Какая-то шестая': [260000, 240000, 310000, 50000000]
}

enterprises.clear()
count_enterprises = int(input('Введите количество предприятий: '))
if count_enterprises <= 0:
    raise ValueError('Должно быть больше нуля!')
for entprs in range(1, count_enterprises + 1):
    name_enterprise = input(f'Введите название предприятия {entprs}: ')
    profit_enterprise = list(map(float, (input(
        'Введите прибыль этого предприятия за 4 квартала (4 отдельных числа, '
        'разделённых пробелом): ').strip().split())))[:4]
    enterprises[name_enterprise] = profit_enterprise

average = get_average(enterprises.values())
print(f'Среднее: {average}')
print('Выше среднего:')
for key, value in enterprises.items():
    if sum(value) > average:
        print(f'{key}, годовой доход: {sum(value)}')
print('Ниже среднего:')
for key, value in enterprises.items():
    if sum(value) < average:
        print(f'{key}, годовой доход: {sum(value)}')
