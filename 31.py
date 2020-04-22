import numpy as np
import random
'''31. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
summ=0
count=0
for i in range(n):
    A[i]=random.randint(0,100)
    if A[i]>=-2 and A[i]<=10:
        summ+=A[i]
        count+=1
        print(A[i])
print(A)
av=summ/count
print('Number:',av)
