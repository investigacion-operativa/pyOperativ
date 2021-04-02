import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import numpy as np

np.random.seed(3)

mu = 0.0
var = 1.0
sigma = math.sqrt(var)

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.title(f"Distribución normal, $\mu$={mu}, $\sigma$={sigma}")
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()


# N = 50
# x = np.random.normal(mu, sigma, N)
# y = np.random.normal(mu, sigma, N)
# plt.scatter(x, y, edgecolors='b')
# plt.show()


# lam_n = 30
# n_lambdas = 30
# lambdas = np.linspace(0, lam_n, n_lambdas)
# x = np.linspace(0, 1, 100)

# for lam in lambdas:
#     plt.plot(x, stats.expon.pdf(x, scale=1/lam))

# plt.title(f"Distribución exponencial, $\lambda$=0-{lam_n}, paso={lam_n/n_lambdas}")
# plt.show()


