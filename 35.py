import numpy as np
import random
'''35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
for i in range(len(A)):
    A[i]=int(input(f'{i}='))
print(A)
count=0
for i in range(len(A)):
    if A[i]<A[i-1] and i!=0:
        count+=1
        if count==len(A)-1:
            print('Sorted')
        continue
    elif A[i]>=A[i-1] and i!=0:
        print('Not sorted')
        break
        
