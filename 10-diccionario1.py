# Creando un diccionario simple
videojuegos = {
    'juego'     :   'Fortnite', #Llave y valor
    'tipo'      :   'Shooter',
    'genero'    :   'Accion',
    'like'      :   3000,
    'lanzamiento':  2017
}
print(videojuegos)

# Accediendo a los elementos del diccionario
print(videojuegos['juego'])
print(videojuegos['genero'])

# Mezclar con un string
megusta = videojuegos['juego']
print(f'Estoy jugando {megusta}')

# Agregar nuevos valores
videojuegos['jugadores'] = 'Muchos'
print(videojuegos)

# Reemplazar valor existente y si no existe lo agrega
videojuegos['like'] = 'Me encorazona'
print(videojuegos)

# Eliminar un valor
del videojuegos['jugadores']
print(videojuegos)