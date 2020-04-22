import numpy as np
import math
'''2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
(Кудрявцев Владислав)'''
X=np.zeros(5, dtype=int)
for i in range (len(X)):
    X[i]=int(input(f'Input X[{i}]='))
n=len(X)
for i in range (n):
    print (f'X[{i}]^2={X[i]**2}')
    X[i]=math.sqrt(X[i])
    print (f'sqrt(X[{i}])={X[i]}')
