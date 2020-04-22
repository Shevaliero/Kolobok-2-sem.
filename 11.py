import numpy as np
'''11. Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=int(input(f'{i+1} day:'))
    if A[i]>20:
        count+=1
print(f'{count} days')
