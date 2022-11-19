while True:
    try:
        seq_numbers = sorted([int(i) for i in input('Введите числа: ').split()])
        if not seq_numbers:
            print('Вы не ввели числа\n'
                  '(необходимо ввести только цифры через пробел)')
        else:
            break
    except ValueError as exp:
        print('Вы ввели недопустимые символы\n'
              '(необходимо ввести только цифры через пробел)')

while True:
    try:
        any_number = [int(i) for i in input('Введите любое число: ').split()]
        if len(any_number) > 1:
            print('Необходимо ввести одно челое число')
        elif not any_number:
             print('Вы не ввели число\n'
                   '(необходимо ввести целое число)')
        else:
            break
    except ValueError as exp:
        print('Вы ввели недопустимые символы\n'
              '(необходимо ввести только целое число)')


def binary_search(array, elem, low, high):
    middle = (low + high) // 2
    if min(array) >= elem[0]:
        return f'Элемент меньше введенного числа отсутствует\n'\
               f'Номер позиции элемента, который больше или равен введенному числу: {low}'
    elif max(array) < elem[0]:
        return f'Элемент больше введенного числа отсутствует\n'\
               f'Номер позиции элемента, который меньше введенного числа: {high}'
    else:
        if low > high:
            return f'Номер позиции элемента, который меньше введенного числа: {middle}\n'\
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle + 1}'
        elif array[middle] == elem[0]:
            return f'Номер позиции элемента, который меньше введенного числа: {middle - 1}\n'\
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle}'
        elif array[middle] > elem[0]:
            return binary_search(array, elem, low, middle - 1)
        else:
            return binary_search(array, elem, middle + 1, high)


print(list(enumerate(seq_numbers)))
print(binary_search(seq_numbers, any_number, 0, len(seq_numbers) - 1))






