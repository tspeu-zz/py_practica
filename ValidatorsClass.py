# import uuid
from random import randint
# , randrange
import datetime
import re
import os.path


"""

"""
def crear_id_ramdom():
    # _id = uuid.uuid4().hex[:8]
    # print("Printing random integer ", randrange(0, 20, 2))
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
    x = datetime.datetime.now().year
    print(f"año actual: {x}")
    if validar_formato_fecha(fecha):
        if int(fecha) < x:
            print(f"fecha nacimiento ok")
            return True


"""
"""
def validated_year(year):
    if len(year) < 4:
        _pos = 4 - len(year)  # 1 - 2 -3
        cont = 0
        _ok = ""
        _fecha = "0001"
        print(_pos)
        for i in range(0, _pos):
            # _fecha = "#" + _fecha + "%"
            _ok += _fecha[i]
            cont += 1
        # print(_fecha)
        print(_ok)
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


# isbna 10
def is_valid_isbn10(isbn):
    # check for length
    if len(isbn ) != 10:
        return False

    # Computing weighted sum
    # of first 9 digits
    _sum = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            _sum += int(isbn[i]) * (10 - i)
        else:
            return False

    # Checking last digit
    if (isbn[9] != 'X' and
            0 <= int(isbn[9]) <= 9):
        return False

    # If last digit is 'X', add
    # 10 to sum, else add its value.
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])

    # Return true if weighted sum of
    # digits is divisible by 11
    return _sum % 11 == 0

# isbna 13
# def is_valid_isbn13(isbn):
def is_valid_isbn13(code):

    result = False

    # isbn13 string have 13 chars. All of them should be numbers.
    if re.match('^\d{13}$', code):
        sum = 0

        # result = (isbn[0] * 1 + isbn[1] * 3 + ... + isbn[12] * 1) mod 10 == 0
        for i in range(len(code)):
            digit = int(code[i])
            sum += digit * (3 if is_odd(i) else 1)

        result = sum % 10 == 0

    return result

#
def is_odd(n):
    return n % 2 != 0

# This code is contributed
# by "Abhishek Sharma 44"

# validar si existe el fichero return True si existe
def validated_file_exist(_file_name):
    return os.path.isfile(_file_name)
