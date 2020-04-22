import numpy as np
import random
'''28. Знайти кількість парних елементів одновимірного масиву.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(0,100)
    if A[i]%2==0:
        count+=1
print(A)
print(f'Number:{count}')
