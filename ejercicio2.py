#Hacer un numero aleatorio entre  1 y 10. luego el hacer que el usuario adivine el numero. La aplicacion debe terminar cuando el usuario adivine


import random

s=random.randint(1,10)

while True:
    n=int(input("adivina el numero del sistema (1,,10):"))
    

    if n==s:
        print("me fregaste")
        break
    else:
        print("te falta mascota")
