import numpy as np
'''1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
(Кудрявцев Владислав)'''
A=np.zeros(5, dtype=int)
for i in range (len(A)):
    A[i]=int(input(f'Input A[{i}]='))
summ=0
for i in range (len(A)):
    if i== len(A)-1:
        print (A[i])
    else:
        print(A[i], end=',')
    summ+=A[i]
mv=summ/len(A)
print(f'Average={mv}')
    




