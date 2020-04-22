import numpy as np
'''46. Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці.
(Кудрявцев Владислав)'''
A=np.array([['Apples','Pineapples'],
            ['Watermelons','Bananas'],
            ['Apples','Strawberry']])
n=len(A)
print(A)
for i in range(n):
    for j in range(n):
        if A[i][0]==A[j][0] and i!=j:
            A[j][0]='-'
            A[i][0]='-'
print(f'Result:\n{A}')
