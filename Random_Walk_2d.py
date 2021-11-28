import random
import pandas as pd
import matplotlib.pyplot as plt


def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'E', 'S', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return x, y


# 坐标点的展示
coordinate = pd.DataFrame({'x轴': [0], 'y轴': [0]})
for i in range(100):
    step_walk = random_walk(20)
    coordinate.loc[i] = step_walk  # 对df新增行时，使用loc[i]。不能使用iloc[i]
    # coordinate = coordinate.append(step_walk,ignore_index=True) 是另一种在df最后添加一行的方法，但step_walk数据类型需要为df

x = coordinate['x轴']
y = coordinate['y轴']
plt.plot(x, y, '*')
plt.show()

