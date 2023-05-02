Base_de_datos = {}
def datos_usuarios():
    NombreDeUsuario = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    Base_de_datos[NombreDeUsuario] = Contraseña

def mostrar_datos():
    for dato in Base_de_datos.keys():
        print("El usuario es: "+ dato + " la contraseña es: " + Base_de_datos[dato])

def login():
    usuario_input = input("Ingrese su nombre de usuario: ")
    if(Base_de_datos.get(usuario_input) == None):
        while Base_de_datos.get(usuario_input) == None:
            usuario_input = input("Usuario incorrecto, ingrese nuevamente el nombre de usuario: ")
        print("Usuario OK")
    password_input = input("Ingrese su contraseña: ")
    while password_input != Base_de_datos[usuario_input]:
            password_input = input("Contraseña incorrecta, ingrese nuevamente la contraseña: ")
    print("Contraseña OK")
    print("Has iniciado sesión")
print("Ingreso de usuarios")
datos_usuarios()
datos_usuarios()
datos_usuarios()
print("Los datos de los usuarios son: ")
mostrar_datos()
print("login de usuarios")
login()