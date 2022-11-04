ticket_price = list({'age < 18' : 'бесплатно', '18 <= age < 25' : 990, 'age >= 25' : 1390}.values())
ticket_cost = 0
for i in range(int(input('Сколько билетов вы хотите приобрести: '))):
    age = int(input(f'Введите ваш возраст для билета {i + 1}: '))
    if age < 18:
        print('Стоимость билета:', ticket_price[0])
        print('---')
    elif 18 <= age < 25:
        ticket_cost += ticket_price[1]
        print('Стоимость билета:', ticket_price[1],'руб.')
        print('---')
    else:
        ticket_cost += ticket_price[2]
        print('Стоимость билета:', ticket_price[2],'руб.')
        print('---')
if i + 1 > 3:
    print('Итого сумма к оплате с учетом скидки:', round(ticket_cost * 0.9),'руб.')
else:
    print(f'Итого сумма к оплате: {ticket_cost} руб.')






