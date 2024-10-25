import random
import string
import os

usuarios_file = 'usuarios.txt'
contraseñas_file = 'contraseñas.txt'

def registrar_usuario(nombre_usuario, contraseña):
    with open(usuarios_file, 'a') as archivo:
        archivo.write(f"{nombre_usuario},{contraseña}\n")

def verificar_usuario(nombre_usuario, contraseña):
    if os.path.exists(usuarios_file):
        with open(usuarios_file, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    usuario, passw = partes
                    if usuario == nombre_usuario and passw == contraseña:
                        return True
    return False

def generar_contraseña(longitud=12):
    if longitud < 4:
        raise ValueError("La longitud debe ser al menos 4 para incluir todos los tipos de caracteres.")
    
    mayusculas = random.choice(string.ascii_uppercase)
    minusculas = random.choice(string.ascii_lowercase)
    digitos = random.choice(string.digits)
    simbolos = random.choice(string.punctuation)

    caracteres_restantes = mayusculas + minusculas + digitos + simbolos + \
        ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud - 4))

    contraseña = ''.join(random.sample(caracteres_restantes, len(caracteres_restantes)))
    return contraseña

def verificar_contraseña(contraseña):
    if len(contraseña) < 10:
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    if not any(c in string.punctuation for c in contraseña):
        return False
    return True

def guardar_contraseña(contraseña):
    with open(contraseñas_file, 'a') as archivo:
        archivo.write(contraseña + '\n')

def cargar_contraseñas():
    if os.path.exists(contraseñas_file):
        with open(contraseñas_file, 'r') as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    return []

def eliminar_contraseña(contraseña_a_eliminar):
    contraseñas = cargar_contraseñas()
    if contraseña_a_eliminar in contraseñas:
        contraseñas.remove(contraseña_a_eliminar)
        with open(contraseñas_file, 'w') as archivo:
            for contraseña in contraseñas:
                archivo.write(contraseña + '\n')
        return True
    return False

def menu():
    while True:
        print("\n--- Pablo Password Manager 1.0 ---")
        print("1. Generar Contraseña")
        print("2. Verificar Contraseña")
        print("3. Guardar contraseña en el archivo")
        print("4. Cargar contraseñas del archivo")
        print("5. Eliminar Contraseña")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            longitud_deseada = int(input("Ingrese la longitud de la contraseña (mínimo 4): "))
            contraseña_segura = generar_contraseña(longitud_deseada)
            print("Contraseña generada:", contraseña_segura)
        
        elif opcion == '2':
            contraseña_a_verificar = input("Ingrese la contraseña a verificar: ")
            if verificar_contraseña(contraseña_a_verificar):
                print("La contraseña es segura.")
            else:
                print("La contraseña no cumple con los criterios de seguridad.")
        
        elif opcion == '3':
            contraseña_a_guardar = input("Ingrese la contraseña a guardar: ")
            guardar_contraseña(contraseña_a_guardar)
            print("Contraseña guardada en el archivo.")
        
        elif opcion == '4':
            contraseñas_cargadas = cargar_contraseñas()
            if contraseñas_cargadas:
                print("Contraseñas cargadas desde el archivo:")
                for contraseña in contraseñas_cargadas:
                    print(contraseña)
            else:
                print("No se encontraron contraseñas en el archivo.")
        
        elif opcion == '5':
            contraseña_a_eliminar = input("Ingrese la contraseña a eliminar: ")
            if eliminar_contraseña(contraseña_a_eliminar):
                print("Contraseña eliminada correctamente.")
            else:
                print("La contraseña no se encontró en el archivo.")
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def inicio_sesion():
    while True:
        print("\n--- Iniciar Sesión ---")
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if verificar_usuario(nombre_usuario, contraseña):
            print("Inicio de sesión exitoso.")
            menu()
            break
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
        
        volver = input("¿Desea volver al menú principal? (si/no): ")
        if volver.lower() == 'si':
            break

def registro():
    while True:
        print("\n--- Registro de Usuario ---")
        nombre_usuario = input("Ingrese un nuevo nombre de usuario: ")
        contraseña = input("Ingrese una nueva contraseña: ")
        registrar_usuario(nombre_usuario, contraseña)
        print("Usuario registrado exitosamente.")

        volver = input("¿Desea volver al menú principal? (si/no): ")
        if volver.lower() == 'si':
            break

def main():
    while True:
        print("\n--- Gestor de Contraseñas ---")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            inicio_sesion()
        elif opcion == '2':
            registro()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()
