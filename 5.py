import numpy as np
import random
'''5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
(Кудрявцев Владислав)'''
A=np.zeros(7,dtype=int)
for i in range(len(A)):
    A[i]=random.randint(-10,10)
print(A)
for i in range(len(A)):
    A[i]*=2
print(A)
