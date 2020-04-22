import numpy as np
import random
'''17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=float)
res=0
for i in range(len(A)):
    A[i]=random.uniform(100,200)   #uniform- модуль для генерации float чисел
    if i%2!=0:
        res+=A[i]
print(A)
print(f'Summ is: {res}')
