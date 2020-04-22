import numpy as np
import random
'''6. Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву.
(Кудрявцев Владислав)'''
A=np.zeros(8,dtype=int)
count=0
for i in range(len(A)):
    A[i]=random.randint(-10,10)
    if A[i]<0:
        count+=1
print (A)
print(f'Negative numbers={count}')
