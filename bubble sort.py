import numpy as np
import matplotlib.pyplot as plt


number_of_items = 15
L = np.random.randint(0, 100, number_of_items)
x = np.arange(0,number_of_items,1)

n = len(L)
for j in range(n):
    for i in range(0,n - j - 1):
        plt.bar(x, L)
        plt.pause(0.05)
        plt.clf()
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]

plt.show()