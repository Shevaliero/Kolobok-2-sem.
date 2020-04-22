import numpy as np
import random
'''15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
summ=0
for i in range(len(A)):
    A[i]=random.randint(100,200)
    if A[i]%2==0:
        summ+=A[i]
print(A)
print(f'Summ is: {summ}')
