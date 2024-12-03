import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

# 参数
mu = np.array([1, 0.5])
cov = np.array([[1, 0.3], [0.3, 1]])
n_samples = 50000

# 生成模拟数据
samples = np.random.multivariate_normal(mu, cov, n_samples)

# 画图
plt.title('mu = [1, 0.5], cov = [[1, 0.3], [0.3, 1]]')
plt.scatter(samples[:500, 0], samples[:500, 1], alpha=0.5)
plt.axis('equal')
plt.show()

plt.clf()

# z = x+y
z = samples[:, 0] + samples[:, 1]
plt.title('z = x + y')

# 绘制理想结果
a = np.arange(-5, 10, 0.01)
b = stats.norm.pdf(a, loc=1.5, scale=math.sqrt(2+2*0.3))
plt.plot(a, b)

plt.hist(z, bins=100, density=True, alpha=0.5)
plt.show()

plt.clf()

