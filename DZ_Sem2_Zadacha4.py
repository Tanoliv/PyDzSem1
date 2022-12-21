#Реализуйте алгоритм перемешивания списка.

import random

print('Вариант 1')
print('Ввод в список рандомных чисел')

list = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f"исходный список:\n {list}")
random.shuffle(list)
print(f"список после перемешивания:\n{list}")

print('Вариант 2')
print('Ввод данных в список с клавиатуры')

list1= input('Введите текст или произвольные числa через пробел: ').split()
print('Исходный список =',list1)
random.shuffle(list1)
print('Список после перемешивания=', list1)
