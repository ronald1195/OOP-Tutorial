"""
Author: Ronald Munoz
Date: NOV/24/2021
""" 
from sys import path
# Import global resources
path.append(".")
import resources

import pytest

# Import working file
"""
    If Statements
"""

def func1():
    """Que se necesita para que este if statement regrese "Correcto"?"""
    flag = 0

    if flag:
        return "Correcto"
    else:
        return "Incorrecto"


def func2():
    """ Cuales numeros hacen que esta funcion regrese "Correcto"?"""
    n = 0

    if n%2 == 0:
        return "Incorrecto"

    return "Correcto"

def transformar_puntos_a_calificacion(puntaje):
    """ 
    El proposito de esta funcion es convertir un puntaje numerico
    a una calificacion en forma alfabetica
    Ejemplo: 
    1. 90 -> A
    2. 93 -> A+
    3. 78 -> C+

    La applicaion debe permitir transformar los siguientes rangos 
    del sistema numerico al alfabetico

    Sistema Alfabetico  |   Sistema Numerico
    --------------------+-------------------
            A+          |       93 - 100
            A           |       90 - 92
            B+          |       87 - 89
            B           |       83 - 86
            B-          |       80 - 82
            C+          |       77 - 79
            C           |       73 - 76
            C-          |       70 - 72
            D+          |       67 - 69
            D           |       63 - 66
            D-          |       60 - 62
            F           |        0 - 59

    1. Todas los puntajes tienen que regresar la letra con el puntaje que corresponde
    2. Si la funcion recibe un numero que no es un entero (int) la funcion debe
       regresar la palabra "Error"
    3. Si la funcion recibe un numero fuera del rango 0 - 100 ya sea mayor o menor
       la funcion debe regresar la palabra "Error"
    """
    pass




if __name__ == "__main__":

    # Display header
    resources.displayLessonIntroMessage(2)




    """
    Tests:
    ** No modifiques la siguiente seccion ** 
    """
    retcode = pytest.main(["-s", "Tests/lesson2_test.py"])
