#Operadores and y or
usuario_logueado = True
usuario_admin = True
if usuario_logueado and usuario_admin:
    print('ADMINISTRADOR')
elif usuario_logueado:
    print('Acceso al sistema')
elif usuario_admin:
    print('Usuario Admin')
else:
    print('Debes iniciar sesion')

#Operadores con or
usuario_logueado = True
usuario_admin = False
if usuario_logueado or usuario_admin:
    print('ADMINISTRADOR')
elif usuario_logueado:
    print('Acceso al sistema')
elif usuario_admin:
    print('Usuario Admin')
else:
    print('Debes iniciar sesion')