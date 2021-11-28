import random
import math


# 较前一版简化了随机游走函数的代码，提高了代码的可读性
def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y


# 计算最终位置距离原点超过10的比例
Count_too_far = 0
random_walk_simulations = 1000
random_walk_limit = 100
farest = 10
for i in range(random_walk_simulations):
    steps = random_walk(random_walk_limit)
    if int(math.sqrt(steps[0]**2+steps[1]**2)) >= farest:
        Count_too_far += 1
    else:
        pass
print('{:%}'.format(Count_too_far/random_walk_simulations))
