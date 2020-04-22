import numpy as np
import random
'''50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
(Кудрявцев Владислав)'''
A=np.array([123,234,345,543,654,865,196,101,204,155])
B=np.zeros(100,dtype=int)
n=len(B)
count=0
for i in range(n):
    B[i]=random.randint(100,999)
    for j in range(len(A)):
        if B[i]==A[j]:
            count+=1
            print(f'{B[i]} is winner!')
if count==0:
    print('''No one win's''')

