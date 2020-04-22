import numpy as np
'''9. З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
(Кудрявцев Владислав)'''
T=np.zeros(13,dtype=int)
t=0
count=0
for i in range(len(T)):
    T[i]=int(input(f'Input temperature for {i+8} hour:'))
    if T[i]<0 and count==0:
        t=i+8
        count+=1
if t!=0:
    print(f'First negative temperature:{t} hour')
else:
    print('No negative temperature detected')
    
    
    
