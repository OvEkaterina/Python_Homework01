# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
n = int (input())

first_half = n // 1000
second_half = n % 1000
summa_first_half = 0
summa_second_half = 0

while first_half > 0 :
    x = first_half % 10
    summa_first_half = summa_first_half + x
    first_half = first_half // 10

while second_half>0 :
    x = second_half % 10
    summa_second_half = summa_second_half + x
    second_half = second_half // 10

if summa_first_half == summa_second_half :
    print("Yes")
else:
    print ("No")