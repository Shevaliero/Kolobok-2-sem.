import numpy as np
import random
'''55. У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
(Кудрявцев Владислав)'''
A=np.zeros(30,dtype=int)
n=len(A)
count=0
for i in range(n):
    A[i]=random.randint(1,8)
    if A[i]>5:
        count+=1
print(A)
k=-1
for i in range(n//2):
    A[i],A[k]=A[k],A[i]
    k-=1
print(A)
print(f'Apartments with more than 5 persons:{count}')
