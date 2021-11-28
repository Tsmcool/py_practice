import random

import matplotlib.pyplot as plt


def give_the_num():
    nums = random.randint(1,100)
    if nums <= 51:
        return False
    else:
        return True


def a_smart_fool(funds,initial_wager,game_count):
    current_game_count = 0
    previous_game = 'win'
    wager = initial_wager
    x, y = [], []
    while current_game_count < game_count:
        if previous_game == 'win':
            if give_the_num():
                funds += wager
                previous_game = 'win'
                wager = initial_wager
            else:
                funds -= wager
                previous_game = 'lose'
                wager *= 2
        else:
            if give_the_num():
                funds += wager
                previous_game = 'win'
                wager = initial_wager
            else:
                funds -= wager
                previous_game = 'lose'
                wager *= 2
        x.append(current_game_count)
        y.append(funds)
        current_game_count += 1
        if funds <= 0 or funds < wager:
            break
    plt.plot(x, y)


i = 0
while i < 100:
    i += 1
    a_smart_fool(10000, 1000, 1000)
plt.xlabel('Times')
plt.ylabel('Funds')
plt.show()
