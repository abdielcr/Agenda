#Agenda Telefonica
#V0.1 BY Abdiel Carrasco

#Importamos el modulo que contiene las funcines.
import funciones

funciones.bienvenidos()

#Seleccion de opcion por usuario
opcion = int(raw_input())
print("Seleccionaste",opcion)
#Fin de Opciones de usuario

#Estructura de control que maneja las funciones a ejecutar.
if opcion == 1:
	funciones.escribir()
elif opcion == 2:	
	funciones.listar()
else:
	funciones.falla()	
#Fin de la estrucrura de control
#Finde de programa  Agenda Telefonica V 0.1	

