import numpy as np
import random
'''37. Розсортуйте заданий лінійний масив по зростанню.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
for i in range(n):
    A[i]=random.randint(-10,10)
print(A)
for i in range(n-1):      #Сортировка выбором
        mn=i                    #Выбор самого первого элемента как минимальный, для сравнения с последующими
        for j in range(i+1,n):
               if A[j] < A[mn]:
                mn=j          #Замена минимального значение, если оно существует
        A[i],A[mn]=A[mn],A[i]    #Перестановка меньшего елемента на перед
print(A)
