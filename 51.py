import numpy as np
import random
'''51. Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
count=0
n=len(A)
for i in range(n):
    A[i]=random.randint(0,50)
    if A[i]>=i+10:
        count+=1
print(A)
B=np.zeros(count,dtype=int)
c=0
for i in range(n):
    if A[i]>=i+10:
        B[c]=A[i]
        c+=1
print(B)
    
    
    
