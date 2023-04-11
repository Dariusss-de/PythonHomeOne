# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

number = int(input("Input number: "))
for i in range(1,number): 
    if i%2==0:print(i)