""""""

"""
Задание 1
Создать функцию get_wallets(), которая возвращает список кошельков из текстового файла.
У функции должен быть необязательный аргумент file_path, который по умолчанию равен "data/wallets.txt",
чтобы можно было в функцию передавать альтернативный путь к файлу.
Функция должна возвращать список кошельков, каждый кошелек должен быть строкой.
Пример:
get_wallets() -> ["0x7448F5a304A684936deD5B762538AE2658B4f2DD", "0x7448F5a304A684936deD5B762538AE2658B4f2DD"]



Задание 2
Написать чекер дропа.
Написать скрипт, который будет при помощи функции get_wallets() получает 2 списка кошельков из файлов:
- wallets.txt - список кошельков для проверки
- zksync_eligibility_list.txt - список кошельков, которые получили дроп
Сравнивает 2 списка кошельков и выводит на экран:
- кошельки которые получили дроп.
- количество кошельков, которые получили дроп.
- процент кошельков которые получили дроп.

В конце создает 2 файла:
- wallets_with_drop.txt - список кошельков, которые получили дроп
- wallets_status.txt - список всех кошельков с проставленным статусом, получил дроп или нет. 
    Пример: 0x7448F5a304A684936deD5B762538AE2658B4f2DD-ELIGIBLE
            0x8548F5a304A684936deD5B762538AE2658B4f7DD-NOT ELIGIBLE


Задание 3 *
Взять официальную базу кошельков и суммы дропов с гитхаба zksync - 
https://github.com/ZKsync-Association/zknation-data/blob/main/eligibility_list.csv.
Сделать чекер, который берет список кошельков из файла wallets.txt и проверяет их наличие в официальной базе, 
а так же сумму дропа.
Скрипт должен выводить кошельки в терминале в формате: кошелек-статус-сумма дропа.
Пример:
0x7448F5a304A684936deD5B762538AE2658B4f2DD-ELIGIBLE-100
0x8548F5a304A684936deD5B762538AE2658B4f7DD-NOT ELIGIBLE-0

В конце нужно написать сколько кошельков получили дроп и какую сумму токенов получил всего со всех 
проверенных кошельков.
Создать файл wallets_status.txt и записать в него все кошельки с проставленным статусом и суммой дропа.
Создать файл wallets_with_drop.txt и записать в него кошельки, которые получили дроп с суммой дропа.
"""