"""
Домашнее задание по dict
"""

# задание 1

"""
Программа на входе спрашивает сколько кошельков сделать и пользователь в терминале вводит число.
Программа создает список кошельков по введенному количеству (реализуйте одной строчкой кода).
Программа создает список балансов кошельков, где баланс это случайное число от 1 до 1000 (реализуйте одной строчкой кода).
Должно получиться 2 списка.
Объедините 2 списка в словарь, где ключ это кошелек, а значение это баланс.
Сделайте программу, которая будет умножать на 2 все четные значения балансов.
Выведите конечный результат в формате "Кошелек {адрес}: баланс {баланс}", каждый элемент с новой строки.
"""
import random
wallets_amount = int(input("Сколько кошельков сделать: "))  # количество кошельков
wallets = ["0x" + "".join([random.choice("abcdef0123456789") for _ in range(40)]) for _ in range(wallets_amount)]  # список кошельков
balances = [random.randint(1, 1000) for _ in range(wallets_amount)]  # список балансов
wallets_balances = dict()  # словарь кошельков и балансов
for wallet, balance in zip(wallets, balances):  # объединение списков в словарь
    wallets_balances[wallet] = balance  # добавление кошелька и баланса в словарь

for wallet, balance in wallets_balances.items():  # умножение на 2 четных значений балансов
    if balance % 2 == 0:  # если баланс четный
        wallets_balances[wallet] = balance * 2  # умножаем на 2

for wallet, balance in wallets_balances.items():  # вывод результата
    print(f"Кошелек {wallet}: баланс {balance}")  # вывод кошелька и баланса

# задание 2

"""
НЕ ПАДАЙТЕ В ОБМОРОК

Пользователь вводит в терминале количество кошельков, минимальное количество транзакций (должно быть равно или больше).
В программе должен быть создан словарь со списком 3 активностей и их РАНДОМНОЙ стоимостью от 10 до 100 единиц 
(стоимость указывается в единицах газа):
swap = 30 (замените на рандомное число от 10 до 100 единиц)
mint_nft = 50 (замените на рандомное число от 10 до 100 единиц)
burn_nft = 65 (замените на рандомное число от 10 до 100 единиц)

Программа создает словарь в котором ключами являются адреса кошельков, а значением словарь в котором:
- словарь с балансами, где ключ это название токена, а значение количество токена, должен быть 2 токена 
-- ETH баланс рандомно от 0,2 до 0,8.
-- USDC баланс рандомно от 0 до 50.
- общее количество транзакций - изначально по 0.
- словарь с транзакциями, где ключ это название транзакции, а значение количества транзакции, изначально по 0.

Программа должна ждать когда будет рабочий газ ниже 30, при этом газ каждую 0,1 секунды обновляется, рандомно увеличиваясь или уменьшаясь на 1,
газ не может быть меньше 10 или больше 50, если он достигает этих значений он должен начать двигаться в противоположную сторону.

Если газ достиг нужного значения, программа должна запустить в работу кошелек.

Кошелек должен выбираться рандомно, среди тех, которые еще не достигли целевого количества транзакций.

Кошелек должен выбирать рандомную активность, отдавая предпочтения тем которые имеют 0 транзакций.
Все транзакции оплачиваются в токене ETH.
Стоимость транзакции считается по формуле (газ * цена транзакции в еденицах газа / 10000).
Если на балансе недостаточно денег для выполнения транзакции нужно сделать вывод с биржи суммы равной транзакции умноженной на 2 + рандомный %,
чтобы сумма вывода была всегда рандомная.

Если выбранная транзакция mint_nft или burn_nft, то нужно только потратить деньги с баланса ETH на комиссию и записать транзакцию в общий счетчик транзакций
и счетчик конкретной активности.

Если транзакция swap нужно сделать обмен обмен:
- если баланс USDC нулевой, то ETH на USDC, рандомную сумму в пределах баланса за вычетом комиссии
- если баланс USDC НЕ нулевой, то все USDC меняем на ETH
Стоимость ETH в USDC должна генерироваться в момент обмена в диапазоне от 2000 до 3000.
Балансы кошелька в обоих токенах должны быть обновлены после обмена.
Не забудьте списать стоимость транзакции с баланса, а так же записать транзакцию в общий счетчик транзакций
и счетчик конкретной активности.

После транзакции ожидайте рандомную паузу от 0,5 до 1,5 секунд перед выбором следующего кошелька.

Программа должна завершиться когда все кошельки сделают минимальное количество транзакций.
Программа должна напечатать в терминале перечисление итоговых данных по всем кошелькам в формате:
Кошелек {адрес}:
--- Баланс ETH: {количество токена}
--- Баланс USDC: {количество токена}
--- Количество транзакций: {количество}
--- Количество транзакций swap: {количество}
--- Количество транзакций mint_nft: {количество}
--- Количество транзакций burn_nft: {количество}

В данной задаче нужно будет гуглить, использовать чат жпт, пытайтесь решать задачу кусками, попробуйте реализовать одну часть, а потом другую.
Можете реализовать не все задания из задачи, но попробуйте.

"""
import random
import time


wallets_amount = int(input("Введите количество кошельков: "))  # количество кошельков
min_transactions = int(input("Введите минимальное количество транзакций: "))  # минимальное количество транзакций
gas = random.randint(10, 50)  # стартовый газ
gas_limit = 30  # целевое значение газа
activities_prises = {
    "swap": random.randint(10, 100),
    "mint_nft": random.randint(10, 100),
    "burn_nft": random.randint(10, 100)
}  # активности и их стоимость

my_wallets = {}  # список кошельков
for i in range(wallets_amount):
    wallet_address = "0x" + "".join([random.choice("abcdef0123456789") for _ in range(40)])  # адрес кошелька
    eth_balance = random.uniform(0.2, 0.8)  # баланс ETH
    usdc_balance = random.randint(0, 50)  # баланс USDC
    # добавление кошелька в словарь и инициализация значений
    my_wallets[wallet_address] = {
        "balances": {"ETH": eth_balance, "USDC": usdc_balance},  # балансы
        "transactions": 0,  # количество транзакций
        "activities": {"swap": 0, "mint_nft": 0, "burn_nft": 0}  # количество транзакций по активностям
    }  # добавление кошелька в словарь

wallets_list = list(my_wallets.keys())  # список кошельков
while True:
    wallet = random.choice(wallets_list)  # выбор случайного кошелька

    while True:  # цикл ожидания газа
        gas += random.choice([-1, 1])
        if gas <= 10:  # если газ равен 10
            gas += 1  # увеличиваем газ
        elif gas >= 50:  # если газ равен 50
            gas -= 1  # уменьшаем газ

        print(f"Газ: {gas}")  # вывод газа
        time.sleep(0.1)  # пауза
        if gas < gas_limit:  # если газ меньше целевого значения
            print("Газ достиг нужного значения")
            break  # завершаем цикл обновления газа

    activities = my_wallets[wallet]["activities"]  # копируем словарь активностей и кол-ва транзакций по ним
    if all(activities.values()) or not any(activities.values()):  # если все активности выполнены или не выполнена ни одна
        random_activity = random.choice(list(activities.keys()))  # выбор случайной активности
    else:
        zero_activities = [activity for activity in activities if not activities[activity]]  # создаем список активностей с 0 транзакций
        random_activity = random.choice(zero_activities)  # выбор случайной активности

    price_activity = activities_prises[random_activity] * gas / 10000  # стоимость активности в ETH

    if price_activity > my_wallets[wallet]["balances"]["ETH"]:  # если стоимость активности больше баланса ETH
        withdraw_amount = price_activity * 2 * random.uniform(1.1, 1.2)  # сумма вывода с биржи
        my_wallets[wallet]["balances"]["ETH"] += withdraw_amount  # добавление суммы вывода на баланс ETH
        print(f"Кошелек {wallet} вывел {withdraw_amount} ETH с биржи для выполнения транзакции {random_activity}")

    if random_activity == "swap":  # если активность swap
        eth_usdc_price = random.randint(2000, 3000)  # стоимость ETH в USDC
        if my_wallets[wallet]["balances"]["USDC"]:  # если баланс USDC не нулевой
            my_wallets[wallet]["balances"]["ETH"] += my_wallets[wallet]["balances"]["USDC"] / eth_usdc_price  # обмен USDC на ETH
            my_wallets[wallet]["balances"]["USDC"] = 0  # обнуление баланса USDC
        else:
            # генерируем случайную сумму обмена между 0 и балансом ETH за вычетом стоимости транзакции
            swap_amount = random.uniform(0, my_wallets[wallet]["balances"]["ETH"] - price_activity)  # сумма обмена
            my_wallets[wallet]["balances"]["ETH"] -= swap_amount  # списываем сумму обмена
            my_wallets[wallet]["balances"]["USDC"] += swap_amount * eth_usdc_price  # добавляем сумму обмена в USDC

    my_wallets[wallet]["balances"]["ETH"] -= price_activity  # списываем стоимость активности с баланса ETH

    print(f"Кошелек {wallet} выполнил активность {random_activity} за {price_activity} ETH")
    my_wallets[wallet]["transactions"] += 1  # увеличиваем количество транзакций
    my_wallets[wallet]["activities"][random_activity] += 1  # увеличиваем количество транзакций по активности

    if my_wallets[wallet]["transactions"] >= min_transactions:  # если количество транзакций достигло минимального
        wallets_list.remove(wallet)  # удаляем кошелек из списка
        if not wallets_list:  # если список пуст
            break  # завершаем программу

    time.sleep(random.uniform(0.5, 1.5))  # пауза

for wallet, data in my_wallets.items():  # вывод результатов
    print(f"Кошелек {wallet}:")
    print(f"--- Баланс ETH: {data['balances']['ETH']}")
    print(f"--- Баланс USDC: {data['balances']['USDC']}")
    print(f"--- Количество транзакций: {data['transactions']}")
    print(f"--- Количество транзакций swap: {data['activities']['swap']}")
    print(f"--- Количество транзакций mint_nft: {data['activities']['mint_nft']}")
    print(f"--- Количество транзакций burn_nft: {data['activities']['burn_nft']}")