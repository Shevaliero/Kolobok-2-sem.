import numpy as np
import random
'''19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.
(Кудрявцев Владислав)'''
A=np.zeros(20,dtype=int)
n=len(A)
res=0
for i in range(n):
    A[i]=random.randint(200,300)
    if A[i]%2==3:
        res+=A[i]
print(A)
print('Summ is:',res)
    
