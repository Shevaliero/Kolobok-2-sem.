import numpy as np
'''12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
summ=0
count=0
for i in range(n):
    A[i]=int(input(f'{i+1} day:'))
    summ+=A[i]
av=summ/n
for i in range(n):
    if A[i]>av:
        count+=1
print(f'{count} times bigger then avarage')
