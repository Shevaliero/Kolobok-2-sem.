import numpy as np
import random
'''22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
res=1
for i in range(n):
    A[i]=random.randint(5,500)
    if A[i]%3==0 and A[i]%9==0:
        res*=A[i]
print(A)
print('Result is:',res)
