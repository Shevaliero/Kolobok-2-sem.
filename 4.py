import numpy as np
'''4. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
(Кудрявцев Владислав)'''
A=np.array(['Johnson','Anderson','Blackwood','Brown','Joestar'])
n=len(A)
u=input('Input first letter of surname:')
for i in range(n):
    if u==A[i][0]:   #Сравнение введенного символа, с первым символом каждого слова
        print(A[i])
