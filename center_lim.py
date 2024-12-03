import numpy as np
import matplotlib.pyplot as plt

# y_1 = 2x 0<x<1
# y_2 = -x -1<x<0 =x 0<x<1

def gen_x1(n):
    return np.sqrt(np.random.random(n)).mean()

def gen_y1(n,iter_num):
    y = []
    for i in range(iter_num):
        x = gen_x1(n)
        y.append(x)
    return np.array(y)

plt.hist(gen_y1(2,100000), bins=100, density=True, alpha=0.5)
plt.title('y1 = 2x, 0<x<1,n=2')
plt.show()

plt.clf()

plt.hist(gen_y1(10,100000), bins=100, density=True, alpha=0.5)
plt.title('y1 = 2x, 0<x<1,n=10')
plt.show()

def gen_x2(n):
    x = np.sqrt(np.random.random(n))
    return np.where(np.random.random(n) < 0.5, -x, x).mean()

def gen_y2(n,iter_num):
    y = []
    for i in range(iter_num):
        x = gen_x2(n)
        y.append(x)
    return np.array(y)

plt.hist(gen_y2(3,100000), bins=100, density=True, alpha=0.5)
plt.title('y2 = |x|, 0< |x|<1,n=3')
plt.show()

plt.clf()
plt.hist(gen_y2(10,100000), bins=100, density=True, alpha=0.5)
plt.title('y2 = |x|, 0< |x|<1,n=10')
plt.show()