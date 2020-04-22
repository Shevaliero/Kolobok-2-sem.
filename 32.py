import numpy as np
import random
'''32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
t=False
for i in range(n):
    A[i]=random.randint(-10,10)
    if A[i]<0 and A[i]%2==0:
        t=True
print(A)
print(t)
    
