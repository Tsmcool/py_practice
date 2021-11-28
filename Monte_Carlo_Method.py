import random

import matplotlib.pyplot as plt


def give_the_num():
    nums = random.randint(1,100)
    if nums <= 51:
        # print(nums, 'you lose,play again')
        return False
    else:
        # print(nums, 'you win,play more')
        return True


def a_fool(funds,wager,game_counts):
    current_game_counts = 0
    x, y = [], []
    while current_game_counts<game_counts:
        if give_the_num():
            funds += wager
            x.append(current_game_counts)
            y.append(funds)
        else:
            funds -= wager
            x.append(current_game_counts)
            y.append(funds)
        current_game_counts += 1
        # if funds <= 0:
        #     break
    plt.plot(x, y)
    # if current_game_counts == game_counts:
    #     return f'now,you play {current_game_counts} times,and you have {funds}'
    # else:
    #     return f'now,you play {current_game_counts} times,and you lose all money'


i = 0
while i <= 1000:
    a_fool(10000, 2000, 1000)
    i += 1
plt.xlabel('times')
plt.ylabel('funds')
plt.show()