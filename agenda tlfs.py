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
#funcion que pinta el menu y devuelve la opcion seleccionada del 1 al 5
def pintaMenu():
    opcion=0
    while (opcion<1 or opcion>5):
        print("*****AGENDA*****")
        print("Pulsa 1 para INSERTAR un contacto")
        print("Pulsa 2 para BORRAR un contacto")
        print("Pulsa 3 para BUSCAR un contacto")
        print("Pulsa 4 para VER todos los contacto")
        print("Pulsa 5 si desea SALIR de su agenda")
        print("************")
        opcion=(int)(input("SELECCIONE UNA OPCION: "))
        try:
            opcion=(int)(input("SELECCIONE UNA OPCION: "))  #si da error lo que hay dentro del try salta
        except:
            print("Las opciones son del 1 al 5")
    
    return opcion


opcion=pintaMenu()
while(opcion!=5):
    opcion=pintaMenu()






#El telefono de juan es: ejercicio casa

print("El teléfono de ", vNombres , "es: ",vTelefonos,)