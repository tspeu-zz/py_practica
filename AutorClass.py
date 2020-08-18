import datetime


class Autor(object):

    def __init__(self, nombre, apellido, i, fecha):
        self.__nombre = nombre
        self.__apellidos = apellido
        self.__id = i
        self.__fecha_n = fecha

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, n):
        self.__nombre = n

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_id(self):
        return self.__id

    def set_id(self, i):
        self.__id = i

    def get_fecha_n(self):
        return self.__fecha_n

    def set_fecha_n(self, fecha_n):
        self.__fecha_n = fecha_n

    """
    Comprobación fecha se usará en el constructor y en el
    setter. Comprobará que tiene una fecha válida anterior a la actual y
    devolverá true o false
    """
    @staticmethod
    def validar_formato_fecha(fecha):
        try:
            date_string = fecha
            # format = "%Y"
            datetime.datetime.strptime( date_string, "%Y")
            print("This is the correct date string format.")
            return True
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            return False

    @staticmethod
    def validar_fecha(fecha):
        x = datetime.datetime.now().year
        print(x)
        if Autor.validar_formato_fecha(fecha) and fecha < x:
            print("OOOKKKK")
