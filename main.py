# zad1
# print('\n zad 1')
# A = [1 - x for x in range(11)]
# B = [4**y for y in range(0,8,1)]
# C = [z for z in B if z % 2 == 0]
# print(A)
# print(B)
# print(C)


# zad2
# print('\n zad 2')
# import random
# lista1 = []
# for x in range(10):
#     x = random.randrange(1, 100)
#     lista1.append(x)
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)

# zad3
# print('\n zad 3')
# produkty = {'jablka':'kg', 'sok':'litry', 'czekolada':'sztuki', 'kiwi':'sztuki'}
# lista = [x for x in produkty if produkty[x] == 'sztuki']
# print(lista)

# zad4
# print('\n zad 4')
# def trojkat(a, b, c):
#     if (a*a) + (b*b) == (c*c):
#         print('trojkat jest prostokatny')
#         return  0;
#     else:
#         print('trojkat NIE jest prostokatny')
#         return 0;
#
# print(trojkat(3,4,5))
# print(trojkat(3,4,9))


# zad5
# print('\n zad 5')
# def trapez(a=12,b=8,h=4):
#     pole = ((a+b)*h)/2
#     return pole
# print(trapez())

# zad6
# print('\n zad 6')
# def funkcja(a = 1, b = 4, ile = 10):
#     ciag = []
#     ciag.append(a)
#     for x in range(1, ile+1, 1):
#         a *= b
#         ciag.append(a)
#     return ciag
# print(funkcja())

# zad7
# print('\n zad 7')
# def funkcja(*liczby, b = 4, a = 1):
#     ciag = []
#     ciag.append(a)
#     for x in liczby:
#         ciag.append(x*b)
#     return ciag
# print(funkcja(1,2,3,4,5))

# zad8
# print('\n zad 8')
# def zakupy(**produkty):
#     print("ilosc produktow: ")
#     print(len(produkty))
#     print("wartosc calkowita: ")
#     suma = 0
#     for x in produkty:
#         suma += produkty[x]
#     return suma
# print(zakupy(chleb = 2.50, mleko = 3.50, jajka = 6))

# zad9
# print('\n zad 9')
# from ciagi import *
#
# print(arytmetyczny.suma(2, 10, 5))
# print(arytmetyczny.nty_wyraz(2, 5, 2))
# print()
# print(geometryczny.suma(2, 2, 4))
# print(geometryczny.nty_wyraz(2, 2, 4))