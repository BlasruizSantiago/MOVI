# Listas con DNI, nombre de usuario y contraseña de los usuarios ya existentes en el sistema
# Migrar a un JSON.
usrDNI = [43123123, 12345678]
usrActivos = ["sblas", "admin"]
passActivos = ["1234", "admin"]

def __main__():
    print("\nBienvenido a MOVI (Movilidad Optimizada Virtual e Integral)\n\n-------------\n\nMenú Incial: \n  1. Loguearse al sistema \n  2. Registrarse\n")
    menuInicio(usrDNI, usrActivos, passActivos)

# Procedimiento de Registro de usuario.
def Register(usrActivos, usrDNI, passActivos):
    dni = int(input("\nIngrese DNI del usuario: "))
    while(dni < 999999 or dni > 99999999):
        dni = int(input("DNI invalido, por favor ingrese nuevamente su dni: "))
    usr = str(input("Ingrese nombre usuario: "))
    passd = str(input("Ingrese una contraseña: "))
    if(existeUsr(dni, usr, usrActivos, usrDNI)):
        print("El nombre de usuarui y/o DNI ya existe en el sistema!\nVolviendo al inicio...")
    else:
        usrDNI.append(dni)
        usrActivos.append(usr)
        passActivos.append(passd)
        print("Usuario creado exitosamente! \nVolviendo al incio...")
    __main__()

# Función que comprueba la existencia del usuario en las listas creadas.
def existeUsr(dni, usr, usrActivos, userDNI):
    res = False
    i = 0
    while (i+1 <= int(len(usrActivos))):
        if(usr == usrActivos[i]):
            if(dni == userDNI[i]):
                res = True
        i += 1
    return res

# Procedimiento de logueo al sistema.
def Logeo (usrActivos, passActivos):
    usr = str(input("\nUsername: "))
    passd = str(input("Password: "))
    while (buscarUsr(usr, passd, usrActivos, passActivos) == False):
        print ("El usuario/contraseña ingresada invalida, por favor vuelva a intentar loguearse")
        usr = str(input("Username: "))
        passd = str(input("Username: "))
    print("Ingresando al sistema!")

# Busca si existe el usuario en el sistema y chequea que la contraseña este bien colocada.
def buscarUsr(usr, passd, usrActivos, passActivos):
    res = False
    i = 0
    while (i+1 <= int(len(usrActivos))):
        if(usr == usrActivos[i]):
            if(passd == passActivos[i]):
                res = True
        i += 1
    return res

def menuInicio(usrDNI, usrActivos, passActivos):
    res = int(input())
    if(res == 1):
        Logeo(usrActivos, passActivos)
    elif(res == 2):
        Register(usrActivos, usrDNI, passActivos)

__main__()