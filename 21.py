import numpy as np
import random
'''21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=float)
n=len(A)
res=1
for i in range(n):
    A[i]=random.uniform(50,100)
print(A)
u=int(input('Input your number:'))
for i in range(n):
    if A[i]<u:
        res*=A[i]
print('Result is:',res)
