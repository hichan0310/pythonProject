import numpy as np
import matplotlib.pyplot as plt

a=np.random.random(100)
b=a*2+(np.random.randn(100)-0.5)*0.1
p=0
lr=0.01
plt.scatter(a, b)

for i in range(1000):
    cost=0
    for j in range(100):
        costt=b[j]-a[j]*p
        cost+=costt
        p -= -costt*a[j]
    print(cost/100)

plt.plot([0, 1], [0, p])
plt.show()

print(p)

