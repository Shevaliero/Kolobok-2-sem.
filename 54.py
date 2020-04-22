import numpy as np
import random
'''54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
for i in range(n):
    A[i]=random.randint(0,100)
print(A)
for i in range(n):
    for j in range(n):
        if A[i]==A[j] and j>i:
            print(f'Here is same element:A[{i}]=A[{j}], {A[i]}={A[j]}')
            
    
