import numpy as np
import random
'''29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
(Кудрявцев Владислав)'''
A=np.zeros(30,dtype=int)
n=len(A)
count=0
a=int(input('Input you number:'))
flag=True       #Переменная для остановки подсчета после дохода до определенного елемента
for i in range(n):
    A[i]=random.randint(0,30)
    if A[i]%2==0 and A[i]!=a and flag==True:
        count+=1
        print(flag)
    if A[i]==a:
        flag=False
        print('FALSE!')
print(A)
print(f'Count is:{count}')
