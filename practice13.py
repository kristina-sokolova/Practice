tickets = int(input("Введите количество билетов:\n"))
cost = 0
result = 0
for i in range(1, tickets + 1):
    age = int(input(f"Введите возраст посетителя для билета номер {i}:\n"))
    if age < 18:
        cost = 0
        result += cost
    elif 18 <= age < 25:
        cost = 990
        result += cost
    elif 25 <= age:
        cost = 1390
        result += cost
if tickets > 3:
    result_1 = int(result - result * 0.1)
    print(f'Общая стоимость билетов со скидкой 10 % равна {result_1} рублей')
else:
    print(f"Общая стоимость билетов равна: {result} рублей")
