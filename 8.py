import numpy as np
import random
'''8. Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
(Кудрявцев Владислав)'''
A=np.zeros(15,dtype=int)
count=0
for i in range(len(A)):
    A[i]=random.randint(-15,30)
print(A)
for i in range(len(A)):
    if A[i]==max(A):
        print(f'Highest element:{A[i]}, index:{i}')
