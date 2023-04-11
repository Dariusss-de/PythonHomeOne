# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x = float(input('Введите координаты по оси x:'))
y = float(input('Введите координаты по оси y:'))

if x > 0 and y >0: print("First quarter")
if x<0 and y>0: print("Second quarter")
if x<0 and y<0: print("Third quarter")
if x>0 and y<0: print("Four quarter")
