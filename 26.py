import numpy as np
'''26. Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T.
(Кудрявцев Владислав)'''
T=np.zeros(6,dtype=float)
n=len(T)
summ=0
for i in range(n):
    T[i]=float(input(f'{i+1} time:'))
    summ+=T[i]
av=summ/n
print('Lower temperature:',min(T),'\nHigher temerature:',max(T),'\nAverage:',av)
