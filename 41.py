import numpy as np
import random
'''41. Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
u=int(input('Enter your number:'))
t=False
count=0
for i in range(n):
    A[i]=random.randint(-10,10)
for i in range(n):
    if A[i]==max(A):
        count+=1
    if count==1 and max(A)<u:
        t=True
print(A)
print('t is:',t)
    
