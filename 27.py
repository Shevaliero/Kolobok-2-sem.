import numpy as np
'''27. Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
(Кудрявцев Владислав)'''
A=np.zeros(12,dtype=int)
n=len(A)
summ=0     #Количество всех дождей за год
nt=0       #Кол-во сухих месяцов
nd=0       #Самый сухой месяц
for i in range(n):
    A[i]=int(input('Input drop times:'))
    summ+=A[i]
    if A[i]<30:
        nt+=1
    if A[i]==min(A):
        nd=i
print(A)
print(f'All drops in year:{summ} \nLess drops:{nt} \nLess drops month:{nd}')
    
    
