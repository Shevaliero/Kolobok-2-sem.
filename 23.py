import numpy as np
import random
'''23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
res=0
summ=0
for i in range(n):
    A[i]=random.randint(5,500)
    summ+=A[i]
print(A)
av=summ/n
print(f'Average is:{av}')
for i in range(n):
    if A[i]<av:
        res+=A[i]
print('Result is:',res)
