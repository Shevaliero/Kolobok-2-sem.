import numpy as np
'''13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.'''
A=np.zeros(15,dtype=int)
for i in range(len(A)):
    A[i]=int(input(f'A[{i}]='))
print(min(A))
