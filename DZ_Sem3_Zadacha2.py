#Задача 2
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


a= input('Введите список из чисел через пробел \n')
a= list(a.split())
a= list(map(int,a))
print('Список А:',a)
b= []

num= len(a)
for i in range(len(a)):
    while i < len(a)/2 and num > len(a)/2:
        num= num-1 
        pr = a[i] * a[num]
        b.append(pr)
        i += 1
print('Список произведений пар чисел списка А:', b)