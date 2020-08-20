from ValidatorsClass import validar_fecha, validar_longitud


class Autor(object):

    def __init__(self, nombre, apellido, id_autor, fecha):
        self.__nombre = nombre
        self.__apellidos = apellido
        self.__id_autor = id_autor
        self.set_fecha_n(fecha)
        # self.__fecha_n = fecha

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, n):
        self.__nombre = n

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_id_autor(self):
        return self.__id_autor

    def set_id_autor(self, i):
        self.__id_autor = i

    def get_fecha_n(self):
        return self.__fecha_n

    def set_fecha_n(self, fecha_n):
        if len(fecha_n) < 4:
            fecha_n = validar_longitud(fecha_n)
        if validar_fecha(fecha_n):
            self.__fecha_n = fecha_n
        else:
            self.__fecha_n = 1900
            print(f"ERROR en el año de nacimiento el año por defecto será: {self.get_fecha_n()}")

    def __str__(self):
        return f"nombre: {self.get_nombre()}, apellidos: {self.get_apellidos()}, autor_id: {self.get_id_autor()}, año de nacimiento: {self.get_fecha_n()}"

    def autor_nombre(self):
        return f"nombre: {self.get_nombre()}, apellidos: {self.get_apellidos()}"

