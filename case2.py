#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

pointax = float(input('Введите координаты точки a по оси x:'))
pointay = float(input('Введите координаты точки a по оси y:'))
pointbx = float(input('Введите координаты точки b по оси x:'))
pointby = float(input('Введите координаты точки b по оси y:'))


import math
distans = math.sqrt((pointax-pointbx)**2+(pointay-pointby)**2)
print(f'Растояние между точкой A до точки B = {distans}' )

