import numpy as np
'''18. Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
res=1
for i in range(n):
    A[i]=int(input(f'A[{i}]='))
    if A[i]<0:
        res*=A[i]
print(A)
print('Result is is:',res)
    
