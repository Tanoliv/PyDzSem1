#Задача 45
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


a= input('Введите список из чисел через пробел \n')
b= list(a.split())
b= list(map(int,b))
print('Список чисел:', b)
b= [b[i] for i in range(len(b)) if i%2!=0]

print('\nСумма элментов на нечетных позициях =', sum(b))