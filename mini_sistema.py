import os
import pickle

TXT_FILE = "pokedex.txt"
BIN_FILE = "stats.bin"



def crear_archivo_texto():
    """Crea el archivo si no existe"""
    if not os.path.exists(TXT_FILE):
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            f.write("=== Mini Pokedex 2.0 ===\n")
        print("Archivo de texto creado")
    else:
        print("Archivo de texto ya existe")


def agregar_elemento_texto(nombre, tipo, anio, creador, descripcion):
    """Agrega un Pokemon (o item) al archivo de texto"""
    try:
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        with open(TXT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{nombre}|{tipo}|{anio}|{creador}|{descripcion}\n")

    except ValueError as e:
        print("Error:", e)


def leer_coleccion_texto():
    """Muestra todo el archivo TXT"""
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            contenido = f.read()
            print("\n--- COLECCION COMPLETA ---")
            print(contenido)
    except FileNotFoundError:
        print("ERROR: El archivo de texto no existe")


def buscar_por_nombre(nombre):
    """Busca un Pokemon por nombre"""
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.lower().startswith(nombre.lower()):
                    print("Encontrado:", linea)
                    return
        print("No se encontro ese elemento")

    except FileNotFoundError:
        print("ERROR: Archivo no encontrado")



def agregar_stats_binario(nombre, poder, rareza):
    """Guarda estadisticas en archivo binario usando pickle"""
    try:
        if poder < 0 or rareza < 1 or rareza > 100:
            raise ValueError("Valores fuera de rango")

        stats = {"nombre": nombre, "poder": poder, "rareza": rareza}

        # append binario
        with open(BIN_FILE, "ab") as f:
            pickle.dump(stats, f)

    except OSError:
        print("Error al abrir el archivo binario.")
    except ValueError as e:
        print("Error:", e)


def mostrar_stats_binario():
    """Lee todo el archivo binario"""
    try:
        with open(BIN_FILE, "rb") as f:
            print("\n--- ESTADISTICAS BINARIAS ---")
            while True:
                try:
                    datos = pickle.load(f)
                    print(datos)
                except EOFError:
                    break
    except FileNotFoundError:
        print("ERROR: El archivo binario no existe")



def menu():
    crear_archivo_texto()

    while True:
        print("""
===== MINI POKEDEX 2.0 =====
1. Agregar Pokemon
2. Mostrar coleccion completa
3. Buscar por nombre
4. Mostrar datos binarios
5. Salir
""")

        try:
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print("Debes ingresar un numero valido.")
            continue

        if opcion == 1:
            print("\n--- Agregar Pokemon ---")
            nombre = input("Nombre: ")
            tipo = input("Tipo: ")
            anio = input("Año de aparicion: ")
            creador = input("Creador/diseñador: ")
            descripcion = input("Descripcion: ")

            agregar_elemento_texto(nombre, tipo, anio, creador, descripcion)

            try:
                poder = int(input("Nivel de poder (0-999): "))
                rareza = int(input("Rareza (1-100): "))
                agregar_stats_binario(nombre, poder, rareza)
            except ValueError:
                print("Error: valores numericos invalidos")

        elif opcion == 2:
            leer_coleccion_texto()

        elif opcion == 3:
            nombre = input("Nombre a buscar: ")
            buscar_por_nombre(nombre)

        elif opcion == 4:
            mostrar_stats_binario()

        elif opcion == 5:
            print("Saliendo del sistema")
            break

        else:
            print("Opcion no valida")


menu()
