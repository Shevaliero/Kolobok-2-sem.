import numpy as np
import random
'''60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(0,5)
print(A)
tr=0
m=0
for i in range(n):
    if A[i]==A[i-1] and i>0:
        count+=1
        if count>tr:
            m=A[i]
            tr=count
    else:
        count=0
print(f'{m} is repeated the most in a row: {tr+1} times')
