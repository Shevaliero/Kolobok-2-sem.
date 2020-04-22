import numpy as np
import random
'''16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
(Кудрявцев Владислав)'''
A=np.zeros(15,dtype=int)
res=1
for i in range(len(A)):
    A[i]=random.randint(10,50)
    if A[i]%7==0:
        res*=A[i]
print(A)
print(f'Result is: {res}')
