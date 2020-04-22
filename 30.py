import numpy as np
import random
'''30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
summ=0
count=0
for i in range(n):
    A[i]=random.randint(0,100)
    if A[i]>A[i-1] and i!=0:
        summ+=A[i]
        count+=1
        print(A[i])
print(A)
av=summ/count
print('Number:',av)
