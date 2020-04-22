import numpy as np
import random
'''52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
(Кудрявцев Владислав)'''
A=np.zeros(100,dtype=int)
count=0
n=len(A)
for i in range(n):
    A[i]=random.randint(0,50)
print(A)
B=np.zeros(n//2,dtype=int)
c=0
for i in range(n):
    if i%2==0:
        B[c]=A[i]
        c+=1
m=max(B)
print(f'Max value of pair number:{m}')
for i in range(n//2):
    if B[i]==m:
        count+=1
if count>1:
    print('''It's not singular''')
    
        
