#Haga un programa que permita ingresar el número de la tabla que desea imprimir (1-12)
# El programa debe preguntar si desea continuar por ejemplo:Ing...... : 55*1=55*2=10...5*12=60
# Desea continuar?? : Si


result=1
while True:
    numero = int(input("Ingrese el número para la tabla:   "))
    for i in range(1,13):
     result=numero*i
     print(f"{numero}  x  {i} =  {result}")

    opcion=input("¿Desea continuar?       ")
    if opcion=="no":
        break

