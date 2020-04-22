import numpy as np
import random
'''42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
(Кудрявцев Владислав)'''
A=np.zeros(10,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(-10,10)
    fi=1                        #Переменная факториала
    for j in range(1,i+1):          #Вычисление факториала
        fi*=j
    if (i**2) < (A[i]*i) and (A[i]*i) < fi:
        count+=1
        print(f'Is suitable for conditions:{A[i]}')
print(A)
print('Values is:',count)
    
