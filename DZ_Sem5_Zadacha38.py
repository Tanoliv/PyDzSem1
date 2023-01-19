
#38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)


str= 'фьво абввова жывл сергейабв Вова Сергей абврвалг'
print(str)
print('индексы пробелов:')
for i, j in enumerate(str):
    if j== ' ':
        print(i,end=',')
        print()
str= str.split()

str= list(filter(lambda x:  'абв' not in x, str))
print(str)
str= ' '.join(str)
print(str)

print('индексы пробелов:')
for i, j in enumerate(str):
    if j== ' ':
        print(i, j, end='')
        print()

