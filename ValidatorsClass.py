# import uuid
from random import randint
# , randrange
import datetime
import re
import os.path
# import isbnlib


"""

"""
def crear_id_ramdom():
    # _id = uuid.uuid4().hex[:8]
    return randint(3, 9999)


"""
:param string msm: acepta un mensaje para poner al input()
:return string. devuelve el valor de entrada si es un número correcto
"""
def input_num(msm):
    _cont = True
    while _cont:
        _str = input(msm)
        if _str.isdigit():
            _cont = False
            return _str


"""
:param string msm: acepta un mensaje para poner al input()
:return string devuelve el valor de entrada si es correcto 
"""
def input_valor(msm):
    _cont = True
    while _cont:
        _str = input(msm)
        if _str:
            _cont = False
            return _str.strip()


"""
:param string msm: acepta un mensaje para poner al input()
:param int _len longitud de la lista
:return string. devuelve el valor de entrada si es un número correcto y es menor que _len
"""
def input_indice(msm, _len):
    _cont = True
    while _cont:
        _str = input(msm)
        if _str.isdigit():
            if int(_str) < _len:
                _cont = False
                return _str
            else:
                print("ERROR - EL ÍNDICE NO ES CORRECTO")


"""
:param string msm: acepta un mensaje para poner al input()
:return string. devuelve el valor de entrada si es un número correcto
"""
def input_isbn(msm):
    _cont = True
    while _cont:
        _str = input(msm)
        if _str:
            if is_valid_isbn(_str):
                if len(_str) == 13:
                    info_isbn_13(_str)
                _cont = False
                return _str
        print("El ISBN no es válido! Iténtelo de nuevo.")


# todo fecha
"""
:param string msm: acepta un mensaje para poner al input()
:return string devuelve el valor de entrada si es correcto 
"""
def input_fecha(msm):
    _cont = True
    while _cont:
        _str = input(msm)
        if _str:
            if _str.isdigit():
                _cont = False
                return _str.strip()


"""
Comprobación fecha se usará en el constructor y en el
setter. Comprobará que tiene una fecha válida anterior a la actual y
devolverá true o false
https://docs.python.org/es/3/library/datetime.html#strftime-strptime-behavior
"""
def validar_formato_fecha(fecha):
    try:
        validated_year(fecha)
        datetime.datetime.strptime(fecha, "%Y")
        print("El formato del año es correcto")
        return True
    except ValueError:
        print("El formato del año es incorrecto. Debe ser YYYY. Ej 1900")
        return False


"""

"""
def validar_fecha(fecha):
    _y = datetime.datetime.now().year
    if validar_formato_fecha(fecha):
        if int(fecha) < _y:
            return True
    else:
        print(f"fecha nacimiento es mayor que año actual{_y}")
        return False



"""
"""
def validated_year(year):
    print(f"-----------------")
    if len(year) < 4:
        print(year)
        _pos = 4 - len(year)  # 1 - 2 -3
        cont = 0
        _ok = ""
        _fecha = "0001"
        _new = "0000"
        _old = year
        print(f"_pos {_pos}")
        for i in range(0, _pos):
            # _fecha = "#" + _fecha + "%"
            print(i)
            _ok += _fecha[i]
            _new = "0"
            cont += 1
        # print(_fecha)
        print(f"OK: {_ok}")
        _ok += year
        print(f"OK: {_ok}")
        print(f"-----------------")
        # while cont < _pos:
        #     _ok += "0"
        #     cont += 1

        # for _l in year:
        #     print(f"menos {_l}")


# todo isbn
def check(isbn):
    check_digit = int(isbn[-1])
    match = re.search(r'(\d)-(\d{3})-(\d{5})', isbn[:-1])
    if not match:
        return False
    digits = match.group(1) + match.group(2) + match.group(3)
    result = 0
    for i, digit in enumerate(digits):
        result += (i + 1) * int(digit)
    return True if (result % 11) == check_digit else False


# validar ISBN
def is_valid_isbn(code):
    code = code.replace('-', '').replace(' ', '')
    return {
        10: is_valid_isbn10,
        13: is_valid_isbn13
    }.get(len(code), lambda n: False)(code)


# isbn 10
def is_valid_isbn10(isbn):
    result = False
    # isbn string have tiene 10 caracteres.
    # Los primeros 9 caracteres deben ser números y el décimo carácter puede ser un número o una 'X'
    if re.match('^\d{9}[\d,X]{1}$', isbn):
        _sum = 0
        # result = (isbn[0] * 1 + isbn[1] * 2 + ... + isbn[9] * 10) mod 11 == 0
        for i in range(0, 9):
            _sum += int(isbn[i]) * (i + 1)
        _sum += 10 if isbn[9] == 'X' else int(isbn[9]) * 10
        result = _sum % 11 == 0
    return result


# isbn 13
def is_valid_isbn13(isbn):
    result = False
    # isbn string tiene 13 caracteres. todos deben ser números.
    if re.match("^\d{13}$", isbn):
        _sum = 0
        # result = (isbn[0] * 1 + isbn[1] * 3 + ... + isbn[12] * 1) mod 10 == 0
        for i in range(len(isbn)):
            digit = int(isbn[i])
            _sum += digit * (3 if is_odd(i) else 1)
        result = _sum % 10 == 0
    return result

# verificar si el numero es impar
def is_odd(n):
    return n % 2 != 0


# validar si existe el fichero return True si existe
def validated_file_exist(_file_name):
    return os.path.isfile(_file_name)


"""
# informa si el isbn 13  no comienza por 978 o 979
"""
def info_isbn_13(_str):
    if not _str.startswith("978", 0, 2) or _str.startswith("979", 0, 2):
        print("El ISBN no comienza con uno de los prefijos 978 o 979 que están reservados para ISBN;\n "
              "aunque el número está validado, no un ISBN correcto")


# test
# isbn = "007462542X"
# isbn13 = "9783161484100"
#
#
# print(isbnlib.is_isbn13('978-3-16-148410-0'))
# print(isbnlib.is_isbn13('9783161484100'))
# print(isbnlib.is_isbn13('2222222222222'))
