
#Crea una funcion que imprima un mensaje de bienvenida.
def mensaje():
    print('Bienvenidos')
mensaje()

#Crea una funcion que tome el nombre de un usuario y lo muestre como mensaje de bienvenida.
def usuario(nombre, apellido):
    print(f'Bienvenido {nombre}, {apellido}')
usuario('Elmer', 'Zeledon')

#Crea una funcion que tome la ultima actividad que hicistes

def saludar(nomb, apell, anim):
    print (f'Hola! {nomb} {apell} Hoy te sientes {anim}')

def bienvenida(nomb, apell, anim):
    print (f'Bienvenido!!! {nomb} {apell}, te sientes {anim}, Siempre hay que buscar el lado bueno de la vida :)')

def despedir(nomb, apell, anim):
    print (f'Adios {nomb} {apell}, dijistes que te sientes {anim}, Pero todo estara mucho mejor')

print ('Ingresa tu nombre:')
nombre = input()
print ('Ingresa tu apellido')
apellido =input()
print(nombre, apellido, ', Como te sientes hoy?')
animo = input()
saludar(nombre, apellido, animo)
bienvenida(nombre, apellido, animo)
despedir(nombre, apellido, animo)