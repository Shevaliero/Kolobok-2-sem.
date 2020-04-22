import random
import numpy as np
'''33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
res=1
for i in range(n):
    A[i]=random.randint(-10,10)
    if A[i]!=0:
        res*=A[i]
print(A)
print(f'Your number:{res}')
