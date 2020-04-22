import numpy as np
'''10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=int(input(f'{i+1} day:'))
    if A[i]<-10:
        count+=1
print(f'{count} times')
    
