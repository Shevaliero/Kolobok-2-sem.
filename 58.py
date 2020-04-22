import numpy as np
import random
''' 58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
(Кудрявцев Владислав'''
A=np.zeros(25,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(0,25)
print(A)
nm=0
for i in range(n):
    tr=0
    for j in range(n):
        if A[j]==A[i] and i!=j:
            tr+=1
        if tr>count:
            nm=A[j]
            count=tr
print(f'{nm} number is repeated the most: {count} times')
    
