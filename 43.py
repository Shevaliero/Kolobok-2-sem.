import numpy as np
import random
'''43. Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
(Кудрявцев Владислав)'''
w=False
a,b=int(input('Input a:')),int(input('Input b:'))
A=np.zeros(15,dtype=int)
n=len(A)
for i in range(n):
    A[i]=random.randint(0,100)
    if A[i]%a==0 and A[i]%b!=0:
        w=True
print(A)
print(f'w is:{w}')
