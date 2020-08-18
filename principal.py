# from ValidatorsClass import *
from AutorClass import *
from LibroClass import *
from ValidatorsClass import *

# todo
"""
El módulo principal contendrá la función main que hará uso de los métodos
de la clase Libro y autor, tendrá un menú para trabajar con Libros y autores
creando listas, con las opciones de crear/modificar y eliminar tanto libros
como autores.
"""

# todo
"""
Creación de ficheros para cargar los datos al programa tanto los libros como
los autores, para ello se contemplarán esta opción en el menú así como se
deberá actualizar los ficheros cuando se agreguen elementos o se actualicen
en el programa.
"""

# contantes
_MSM = "Escojer una opción:\n"
__MENU_NAME = f"{_MSM}[1]:Mostrar Libros\n[2]:Crear Libro\n[3]:Modificar Libro\n[4]:Eliminar Libro\n" \
              f"[5]:Mostrar Autores\n[6]:Crear Autor\n[7]:Modificar Autor\n[8]:Eliminar Autor\n" \
              f"[9]:Cargar Datos Libros\n[10]:Grabar Datos Libros\n[x] SALIR\n"
__ISBN_NAME = "introducir el ISBN: "
__TITULO_NAME = "introducir el TITULO: "
__ID_AUTOR_NAME = "introducir el ID_AUTOR: "
__NAME_AUTOR_NAME = "introducir el Nombre del AUTOR: "
__APELLIDOS_AUTOR_NAME = "introducir el/los apellido/s del AUTOR: "
__FECHA_AUTOR_NAME = "introducir la fecha de nacimiento del AUTOR: "
__MMS_ERROR = "No se han encontrado "
__LIBROS__NAME = "libros"
__AUTORES__NAME = "autores"


# constantes


"""
"""
def crear_libro(isbn, titulo, id_autor):
    return Libro(isbn, titulo, id_autor)


"""
"""
def datos_libros():
    isbn = input_valor(__ISBN_NAME)
    titulo = input_valor(__TITULO_NAME)
    id_autor = input_valor(__ID_AUTOR_NAME)
    return [isbn, titulo.title(), id_autor]


"""
"""
def crear_autor(nombre, apellido, id_a, fecha):
    return Autor(nombre, apellido, id_a, fecha)


"""
"""
def datos_autor():
    nombre = input_valor(__NAME_AUTOR_NAME)
    apellido = input_valor(__APELLIDOS_AUTOR_NAME)
    id_a = input_valor(__ID_AUTOR_NAME)
    fecha = input_valor(__FECHA_AUTOR_NAME)
    return [nombre, apellido, id_a, fecha]


"""
:param list() _list lista 
 si existe se muestra cada item
"""
def mostrar_lista(_lista, clase):
    _cont = 0
    if _lista:
        for elem in _lista:
            print(f"[{_cont}] {elem.__str__()}")
            _cont += 1
    else:
        print(f"{__MMS_ERROR} {clase}")


def menu():
    continuar = True
    __libros = []
    __autores = []
    while continuar:
        opcion = input(__MENU_NAME)
        if opcion == "1":
            print("mostrar libros!")
            mostrar_lista(__libros, __LIBROS__NAME)
        elif opcion == "2":
            print("crear libros!!")
            _l = datos_libros()
            __libros.append(crear_libro(_l[0], _l[1], _l[2]))
        elif opcion == "3":

            print("modificar libros!!")
        elif opcion == "4":

            print("borrar libros!")
        elif opcion == "5":
            print("mostrar AUTOR!")
            mostrar_lista(__autores, __AUTORES__NAME)

        elif opcion == "6":
            _f = input("ingrese fechas de nacimiento autor: ")
            Autor.validar_fecha(_f)
            pass
        elif opcion == "7":
            print("modificar AUTOR!")


        elif opcion == "8":
            print("eliminar AUTOR!")

            pass
        elif opcion == "9":
            print("Cargar Datos Libros")

        elif opcion == "10":
            print("GUARDAR Datos Libros")
        else:
            if opcion == "X" or opcion == "x":
                print("Salimos de programa!")
                continuar = False
            else:
                print("LA OPCIÓN NO ES VÁLIDA!")




menu()