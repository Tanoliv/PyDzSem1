'''
40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Модуль сжатия:
Для чисел:
Входные данные:
111112222334445
Выходные данные:
5142233415
Также должно работать и для букв:
Входные данные:
AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
Выходные данные:
6A1F2D7C1A17E
(5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

'''


def cod(txt):
    col = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            col += 1
        else:
            res = res + str(col) + txt[i]
            col = 1
    if col > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(col) + txt[-1]
    return res


def decod(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


text = input("Введите текст для сжатия: ")
print(f"Текст после сжатия: {cod(text)}")
print(f"Возвращенный исходный текст: {decod(cod(text))}")