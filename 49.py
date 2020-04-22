import numpy as np
'''49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
(Кудрявцев Владислав)'''
A=np.array(['Bus','Taxi','Train','Plane','Rocket'])
B=np.array([10,20,40,80,160])
n=len(A)
G=int(input('Input UAH:'))
for i in range(n):
    if B[i]>=G:
        for j in range(i):
            A[j],B[j]='',0
        break
print(f'A={A}\nB={B}')
    
