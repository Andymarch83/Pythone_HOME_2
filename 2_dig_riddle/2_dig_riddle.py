total = int(input('Введите сумму чисел: '))
product = int(input('Введите произведение чисел: '))
for x in range(1, 100):
    for y in range(x, 100):
        if total == (x + y) and product == (x * y):
            print(f'Загаданные числа: {x} и {y}')
