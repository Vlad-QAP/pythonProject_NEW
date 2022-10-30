per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму:'))
per_cent_values = list(per_cent.values())
deposit = list(map(lambda x: x * money/100, per_cent_values))
print('Накопленные средства за год вклада в каждом из банков:', list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать:', max(list(map(int, deposit))))










