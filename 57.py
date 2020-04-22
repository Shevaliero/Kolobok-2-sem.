import numpy as np
'''57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
(Кудрявцев Владислав)'''
A=np.array(['Johnson','Anderson','Blackwood','Brown','Joestar'])
B=np.array([55,45,40,80,160])
n=len(A)
av=sum(B)/len(B)
count=0
count2=0
for i in range(n):
    if B[i]<=av+20 and B[i]>=av-20:   #Найменьшее отклонение от среднего значения
        print(f'Worker with ~average salary: {A[i]}')
    for j in range(n):
        if B[j]>B[i]:
            count+=1
            if count==n:
                print(f'Worker with highest salary - {A[j]}: {B[j]}')
            elif count==n-1:
                print(f'Worker with top 2 salary - {A[j]}: {B[j]}')
        if B[j]<B[i]:
            count2+=1
            if count2==n:
                B[j],A[j]=0,''
print(A,'\n',B)
    
    
    

