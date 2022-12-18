#DZ 5
#Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#Первый вариант - пользователь сам вводит варианты предиктат

print('Введите произвольно первое  высказывание  Истина или Ложь: \n')
x = input()
print('Введите второе высказывание  Истина или Ложь: \n')
y = input()
print('Введите третье высказывание  Истина или Ложь: \n')
z = input()

F1 =  not (x or y or z)

F2 =   x and  not y and not z
   
if F1 == F2:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
else:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - ложно')

#Второй вариант

x = 4
y = 3
z = 4
F1 = not (x or y or z)
F2 = not x and not y and not z


if F1 == F2:
    print('Утверждение истинно')
else:
     print('Утверждение ложно')
  
#Третий вариант

F1 =  not (x or y or z)
F2 =   x and  not y and not z

mass = list['x== False,  y== False,  z== False', 
'x== True ,  y== False,  z== False', 'x== True,  y== True,  z== False',
'x== True,  y== True,  z== True', 'x== False,  y== True,  z== False', 'x== False,  y== False,  z== True',
'x== True,  y== False,  z== True', 'x== False,  y== True,  z== True']

for i in mass:
    if   F1 == F2:
        print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
    else:
        print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - ложно')