import numpy as np
import matplotlib.pyplot as plt

a=np.random.random(100)
b=a*2+(np.random.randn(100)-0.5)*0.1+2
p=[0, 0]
lr=0.01
plt.scatter(a, b)

for i in range(1000):
    cost=0
    for j in range(100):
        costt=a[j]*p[0]+p[1]-b[j]
        cost+=costt
        p[0] -= costt*a[j]*lr
        p[1] -= costt*lr
    print(cost/100)

plt.plot([0, 1], [p[1], p[0]+p[1]])
plt.show()

print(p)

