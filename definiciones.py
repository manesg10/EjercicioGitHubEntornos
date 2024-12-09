import random
print("Hola")
#Definicion de variables
x = 2.5
r = 2
sal = "Francisco"
bol = False
if bol:
    print("Verdad")
print(sal)
res = x + r
print(res)
#Para pedir por pantalla un dato usamos input
edad = int(input("Dime tu edad"))
print(edad)

# condicionales
if edad < 18 or edad == 25:
    print("menor")
elif edad > 65:
    print("Eres un abuelo")
else:
    print("mayor")

'''
Escribe un programa que recorra los números del 1 al 20 y haga lo siguiente:
Si el número es divisible por 3, imprime "Fizz".
Si el número es divisible por 5, imprime "Buzz".
Si el número es divisible por ambos, imprime "FizzBuzz".
En otros casos, imprime el número.

SOLUCIÓN
'''
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

