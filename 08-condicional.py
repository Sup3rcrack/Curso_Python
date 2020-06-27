#Revisar si un condicional es mayor  a
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No puedes pagar')

#Conteo de likes mayor o igual a
like = 200
if like >= 200:
    print('Muy bien llegastes a los 200 likes')
else:
    print('Nadie te quiere jaja')

#if con Textos si cumple la condicion
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Excelente eres un crack')

#Evaluar un Booleano
usuario_autenticado = True
if usuario_autenticado ==True:
    print('usuario autenticado')
else:
    print('Neel, vuelve a autenticarte')

usuario_autenticado = True
if usuario_autenticado ==False:
    print('usuario autenticado')
else:
    print('Neel, vuelve a autenticarte')

#Evaluar un elemento en una lista

lenguajes = ['Python', 'Kotlin', 'JavaScript', 'Ruby', 'R', 'React', 'PHP']
if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('PHP no esta en la lista')

# if Anidados
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

usuario_autenticado = False
usuario_admin = False
if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')