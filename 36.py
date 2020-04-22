import numpy as np
'''36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
summ=0
for i in range(n):
    A[i]=int(input(f'A[{i}]='))
    if A[i]>0:
        summ+=A[i]
print(A)
print(f'Summ is:{summ}')
    
