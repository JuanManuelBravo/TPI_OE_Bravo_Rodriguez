import csv
import os
from datetime import datetime

ARCHIVO_USUARIOS = "data/usuarios.csv"
ARCHIVO_SOLICITUDES = "data/solicitudes.csv"


def cargar_usuarios():
    usuarios = {}
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuarios[row["nombre"]] = {"dias": int(row["dias"])}
    else:
        os.makedirs("data", exist_ok=True)
        with open(ARCHIVO_USUARIOS, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "dias"])
            writer.writerow(["juan", 10])
            writer.writerow(["ana", 5])
            writer.writerow(["pedro", 20])
        usuarios = {"juan": {"dias": 10}, "ana": {"dias": 5}, "pedro": {"dias": 20}}
    return usuarios


def guardar_usuarios(usuarios):
    os.makedirs("data", exist_ok=True)
    with open(ARCHIVO_USUARIOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "dias"])
        for nom, datos in usuarios.items():
            writer.writerow([nom, datos["dias"]])


def registrar_solicitud(nombre, dias, resultado):
    os.makedirs("data", exist_ok=True)
    existe = os.path.exists(ARCHIVO_SOLICITUDES)
    with open(ARCHIVO_SOLICITUDES, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["fecha", "nombre", "dias", "resultado"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), nombre, dias, resultado])


# Estados del sistema
INICIO = "INICIO"
PEDIR_DIAS = "PEDIR_DIAS"
VALIDAR = "VALIDAR"
APROBACION = "APROBACION"
APROBADO = "APROBADO"
RECHAZADO = "RECHAZADO"


def pedir_usuario(usuarios):
    nombre = input(" Ingresa tu nombre: ").lower()
    if nombre in usuarios:
        print(f"Hola {nombre}")
        return nombre
    else:
        print(" Usuario no encontrado")
        return None


def pedir_dias():
    try:
        dias = int(input(" ¿Cuantos dias queres solicitar? "))
        if dias <= 0:
            print(" Debe ser un numero mayor a 0")
            return None
        return dias
    except ValueError:
        print(" Error, ingresa un numero valido")
        return None


def obtener_dias_disponibles(usuario, usuarios):
    return usuarios[usuario]["dias"]


def validar_dias(usuario, dias_solicitados, usuarios):
    dias_disponibles = obtener_dias_disponibles(usuario, usuarios)
    if dias_solicitados > dias_disponibles:
        return False
    return True


def requiere_aprobacion(dias_solicitados):
    return dias_solicitados > 7


def aprobacion_jefe():
    decision = input(" El jefe aprueba? (si/no): ").lower()
    return decision == "si"


def aplicar_descuento(usuario, dias_solicitados, usuarios):
    usuarios[usuario]["dias"] -= dias_solicitados


def chatbot():
    usuarios = cargar_usuarios()

    estado = INICIO
    usuario = None
    dias_solicitados = 0

    print(" Bienvenido al Bot de Vacaciones")
    print("----------------------------------")

    while True:
        if estado == INICIO:
            usuario = pedir_usuario(usuarios)
            if usuario:
                estado = PEDIR_DIAS


        elif estado == PEDIR_DIAS:
            dias_disponibles = obtener_dias_disponibles(usuario, usuarios)
            print(f" Dias disponibles: {dias_disponibles}")
            
            dias = pedir_dias()
            if dias:
                dias_solicitados = dias
                estado = VALIDAR

        elif estado == VALIDAR:
            if validar_dias(usuario, dias_solicitados, usuarios):
                estado = APROBACION
            else:
                estado = RECHAZADO

        elif estado == APROBACION:
            if requiere_aprobacion(dias_solicitados):
                print(" Se requiere aprobacion del jefe")
                if aprobacion_jefe():
                    estado = APROBADO
                else:
                    estado = RECHAZADO
            else:
                estado = APROBADO

        elif estado == APROBADO:
            if usuario is not None:
                aplicar_descuento(usuario, dias_solicitados, usuarios)
                guardar_usuarios(usuarios)
                registrar_solicitud(usuario, dias_solicitados, "aprobado")
                restantes = usuarios[usuario]["dias"]
                print(" Solicitud APROBADA")
                print(f" Dias restantes: {restantes}")
                print(" Fin del proceso")
                estado = INICIO
            else:
                estado = INICIO
                continue


        elif estado == RECHAZADO:
            if dias_solicitados > 0:
                registrar_solicitud(usuario, dias_solicitados, "rechazado")
            print(" Solicitud RECHAZADA")
            print(" Fin del proceso")
            estado = INICIO



if __name__ == "__main__":
    chatbot()
