import numpy as np
import random
from collections import Counter
'''59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
h=0
for i in range(n):
    A[i]=random.randint(0,10)
print(A)
c=Counter(A)       #Считает количество каждого элемента в массиве 
for i in range(n):
    if c[i]>1:     #Если элемент 1, то ничего не меняет, но при большем количестве увеличивает цифру, которая будет отниматся от кол-ва всех чисел в массиве
        h+=c[i]
print(f'{n-h} numbers is unique')
