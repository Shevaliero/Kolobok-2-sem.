import numpy as np
import random
'''44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
(Кудрявцев Владислав)'''
A=np.zeros(15,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(0,10)
    if A[i]==i and A[i]%3==0:
        count+=1
print(A)
print(f'This numbers is:{count}')
        
