import numpy as np
import random
'''56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
r=False
for i in range(n):
    A[i]=random.randint(0,20)
    if A[i]==A[i-1] and A[i]==A[i-2] and i-1>0:
        r=True
print(A)
print(f'r={r}')
