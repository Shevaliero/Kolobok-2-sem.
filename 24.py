import numpy as np
import random
'''24. Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
(Кудрявцев Владислав)'''
A=np.zeros(30,dtype=int)
n=len(A)
summ=0
for i in range(n):
    A[i]=random.randint(500,1000)
    if A[i]%5==0 and A[i]%8==0:
        summ+=A[i]
print(A)
print('Summ is:',summ)
