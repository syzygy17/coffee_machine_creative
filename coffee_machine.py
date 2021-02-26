def print_coffee_machine(water, milk, beans, cups, money):
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'${money} of money')
    print()


def remaining(water, milk, beans, cups, money):
    print_coffee_machine(water, milk, beans, cups, money)


def print_action():
    print('Write action (buy, fill, take, remaining, exit):')


def buy(water, milk, beans, cups, money):
    coffee_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    if coffee_choice == 'back':
        pass
    else:
        coffee_choice = int(coffee_choice)
        if coffee_choice == 1:
            if water - 250 < 0:
                print('Sorry, not enough water!')
            elif beans - 16 < 0:
                print('Sorry, not enough beans!')
            elif cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
        elif coffee_choice == 2:
            if water - 350 < 0:
                print('Sorry, not enough water!')
            elif milk - 75 < 0:
                print('Sorry, not enough milk!')
            elif beans - 20 < 0:
                print('Sorry, not enough beans!')
            elif cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups -= 1
        elif coffee_choice == 3:
            if water - 200 < 0:
                print('Sorry, not enough water!')
            elif milk - 100 < 0:
                print('Sorry, not enough milk!')
            elif beans - 12 < 0:
                print('Sorry, not enough beans!')
            elif cups < 1:
                print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1
    return water, milk, beans, cups, money


def fill(water, milk, beans, cups):
    water += int(input('Write how many ml of water do you want to add:'))
    milk += int(input('Write how many ml of milk do you want to add:'))
    beans += int(input('Write how many grams of coffee beans do you want to add:'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:'))
    return water, milk, beans, cups


def take(money):
    print(f'I gave you ${money}')
    money = 0
    return money


water = 400
milk = 540
beans = 120
cups = 9
money = 550
actions = ["buy", "fill", "take", "remaining", "exit"]

while True:
    print_action()
    action = input()
    if action == actions[0]:
        water, milk, beans, cups, money = buy(water, milk, beans, cups, money)
    elif action == actions[1]:
        water, milk, beans, cups = fill(water, milk, beans, cups)
    elif action == actions[2]:
        money = take(money)
    elif action == actions[3]:
        remaining(water, milk, beans, cups, money)
    elif action == actions[4]:
        break
