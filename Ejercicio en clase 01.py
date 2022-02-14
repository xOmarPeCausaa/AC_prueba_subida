#Haga un programa que permita ingresarel monto del básico de 1 trabajador,
# Su estado civil (1=casado; 2=soltero)Su grado de instrucción (1=Licenciado; 2=Bachiller;3=Técnico)
# Si Casado 10% Bonificación al básicoSi Soltero 5% Bonificación al básicoSi Licenciado 16% Bonificación al básico
# Si Bachiller 8% Bonificación al básicoSi Técnico 4% Bonificación al básico Mostrar
# Bonificación al EC Mostrar Bonificación al GI Mostrar Total

monto_basico=int(input("Ingrese el monto basico del trabajador: "))

print("Estado civil: ")
print("(1) Casado ")
print("(2) Soltero")
opcion_estado_civil=int(input("Ingrese su opcion correspondiente: "))

if  opcion_estado_civil == 1 :

    bonificacion_EC=monto_basico*0.1
elif opcion_estado_civil==2:

    bonificacion_EC=monto_basico*0.05
else:

    bonificacion_EC=0
    print("DATO ERRONEO")

print("Grado de Instruccion: ")
print("(1) Licenciado ")
print("(2) Bachiller")
print("(3) Tecnico")
opcion_grado_inst=int(input("Ingrese su opcion correspondiente: "))

if opcion_grado_inst==1:

    bonificacion_GI=monto_basico*0.16
elif opcion_grado_inst==2:

    bonificacion_GI = monto_basico*0.08
elif opcion_grado_inst == 3:
    bonificacion_GI = monto_basico * 0.04

else:

    bonificacion_GI = 0
    print("DATO ERRONEO")


final_total=monto_basico+bonificacion_GI+bonificacion_EC

print(f"La bonificacion de estado civil es de {bonificacion_EC} soles.")
print(f"La bonificacion de grado de instrucion es de {bonificacion_GI} soles.")
print(f"El total es de {final_total} soles.")