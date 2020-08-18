# from ValidatorsClass import *

class Libro(object):

    def __init__(self, isbn, titulo, id_autor):
        # super().__init__()
        # self.__isbn = isbn
        # self.__titulo = titulo
        # self.__id_autor = id_autor
        self.set_isbn(isbn)
        self.set_titulo(titulo)
        self.set_id_autor(id_autor)

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        if self.validar_isbn_10(isbn) or self.validar_isbn_10(isbn):
            self.__isbn = isbn
        else:
            raise Exception(f"ERROR no puede crear {type(self).__name__}")

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if titulo:
            self.__titulo = titulo
        else:
            raise Exception(f"ERROR no puede crear {type( self ).__name__}")

    def get_id_autor(self):
        return self.__id_autor

    def set_id_autor(self, id_autor):
        if id_autor.isdigit():
            self.__id_autor = int(id_autor)
        else:
            raise Exception(f"ERROR no puede crear {type(self).__name__}")

    def __str__(self):
        return f"título: {self.get_titulo()}, isbn: {self.get_isbn()}, autor_id: {self.get_id_autor()}"

    """
    Comprobará que tiene un formato ISBN-10 válido y devolverá
    true o false en los casos correspondientes.
    """
    @staticmethod
    def validar_isbn_10(isbn):
        if isbn:
            return True

    """
    .Comprobará que tiene un formato ISBN-13 válido y devolverá
    true o false en los casos correspondientes
    """
    @staticmethod
    def validar_isbn_13(isbn):
        if isbn:
            return True
