import numpy as np
import random
'''20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=float)
n=len(A)
res=0
for i in range(n):
    A[i]=random.uniform(50,100)
print(A)
u=int(input('Input your number:'))
for i in range(n):
    if A[i]>u:
        res+=A[i]
print('Summ is:',res)
