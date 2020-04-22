import numpy as np
import random
'''7. Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
(Кудрявцев Владислав)'''
A=np.zeros(12,dtype=int)
B=np.copy(A)
count=0
for i in range(len(A)):
    A[i]=random.randint(-20,10)
    B[i]=A[i]
    if A[i]<0:
        B[i]=0
print(A)
print(B)
