import numpy as np
import random
'''34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
B=np.zeros(10,dtype=int)
C=np.zeros(10,dtype=int)
n=len(A)
for i in range(n):
    A[i],B[i]=random.randint(0,30),random.randint(0,30)
    C[i]=A[i]*B[i]
print('A=',A)
print('B=',B)
print('C=',C)
    
    
