import numpy as np
import random
'''25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
res=1
for i in range(n):
    A[i]=random.randint(10,100)
    if A[i]%5==0:
        res*=A[i]
print(A)
print('Result is:',res)
