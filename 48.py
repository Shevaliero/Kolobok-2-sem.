import numpy as np
'''48. Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
(Кудрявцев Владислав)'''
A=np.array(['Johnson','Anderson','Blackwood','Brown','Skywalker','Appleman'])
n=len(A)
print(A)
k=-1
for i in range(n//2):
    A[i],A[k]=A[k],A[i]
    k-=1
print(A)
