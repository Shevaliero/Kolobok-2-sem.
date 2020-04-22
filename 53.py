import numpy as np
import random
'''53. В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
(Кудрявцев Владислав)'''
u=int(input('Input array length:'))
A=np.zeros(u,dtype=int)
for i in range(u):
    rd=random.randint(0,1)
    if rd==0:
        A[i]=random.randint(0,1)
    elif rd==1:
        A[i]=5
print('A=',A)
for i in range(u):
        for j in range(u):     
            if A[j]<A[j-1] and j!=0:
                A[j],A[j-1]=A[j-1],A[j]
print(A)
