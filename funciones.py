#Mensaje de Bienvenida y opciones de usuario
def bienvenidos():
	print("Bienvenido a Agenda Telefonica")
	print("Selecciona una Opcion")
	print("1  Ingresar un registro a la agenda")
	print("2  Ver los numeros de la agenda")
#Fin de Bienvenida

#Definicion de Funciones que implementan el proceso
def escribir():
	print("Introduce un registro")
	agenda = open("agendatelefonica.csv",'a')
	nombre = raw_input("Nombre de Contacto:")
	telefono = raw_input("Introduce un Telefono:")
	print("Se ha guardado en la agenda el contacto:",nombre,"con el numero",telefono)
	agenda.write(nombre)
	agenda.write(",")
	agenda.write(telefono)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	
def listar():
	print("Lista de contactos")
	agenda = open("agendatelefonica.csv")
	numero = 0
	while numero < 25:
		print (agenda.readline())
		numero = numero + 1
	print("Listado correctamente")	
	agenda.close()

def falla():
	print("La seleccion es incorrecta")	
#Fin de Funciones.