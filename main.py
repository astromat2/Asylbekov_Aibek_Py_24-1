from casino_logic import bet
from decouple import config

money = int(config('MY_MONEY'))
while True:
    if money <= 0:
        print('Вы обанкротились!')
        break
    command = input(f'Хотите запустить аппарат (на счету {money}$)? (Да/Нет)')
    if command.lower() == 'да':
        slot = input('Введите слот для ставки: ')
        if slot.isnumeric() and 1 <= int(slot) <= 30:
            amount = input(f'Введите сумму ставки: ')
            if amount.isnumeric() and 1 <= int(amount) <= money:
                money += bet(int(slot), int(amount))
            else:
                print('Неправильна введена сумма ставки!')
        else:
            print('Неправильно введен слот для ставки!')
    else:
        break

print(f'У вас осталось {money}$.')