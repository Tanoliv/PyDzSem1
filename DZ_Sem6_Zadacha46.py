#Задача 46
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


a= input('Введите список из чисел через пробел \n')
a= list(a.split())
a= list(map(int,a))
print('Список А:',a)

b= [a[i] for i in range(len(a)) if  i < len(a)/2 ]
c= list(reversed([a[i] for i in range(len(a)) if  i >= len(a)/2 ]))

pr_par=list(x*y for x,y in zip(b,c))


print('Список произведений пар чисел списка А:', pr_par)