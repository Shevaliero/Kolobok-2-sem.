import numpy as np
import random
'''47. У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
(Кудрявцев Владислав)'''
A=np.zeros(15,dtype=int)
n=len(A)
for i in range(n):
    A[i]=random.randint(0,30)
m=max(A)
print(A)
print(f'Max:{m}')
fl=True
B=np.zeros(n+1,dtype=int)
for i in range(n):
    if A[i]==m and fl==True:
        fl=False
        B[i],B[i+1]=m,i
        for k in range(i,n+1):
            if k+1<n:
                B[k+2]=A[k+1]
        for j in range(i):
            B[j]=A[j]
print(B)
    
