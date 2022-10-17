'''
Opcion 1:
Lista para nombres
Lista para telefonos

Opcion 2:
Lista para nombres [Juan-telefono, Pepe-telefno]

'''

#Opcion 1:
vNombres = []
vTelefonos = []

#Creamos el menu de la agenda
'''
1-Insertar contacto
2-Borrar contacto
3-Buscar contacto
4-Ver todos los contactos
5-Salir
'''
opcion=0

while (opcion!=5):
    print("Pulsa 1 para INSERTAR un contacto")
    print("Pulsa 2 para BORRAR un contacto")
    print("Pulsa 3 para BUSCAR un contacto")
    print("Pulsa 4 para VER todos los contacto")
    print("Pulsa 5 si desea SALIR de su agenda")
    opcion=(int)(input("SELECCIONE UNA OPCION: "))
    try:
        opcion=(int)(input("SELECCIONE UNA OPCION: "))
    except:
        print("Las opciones son del 1 al 5")






#El telefono de juan es: ejercicio casa

print("El teléfono de ", vNombres , "es: ",vTelefonos,)