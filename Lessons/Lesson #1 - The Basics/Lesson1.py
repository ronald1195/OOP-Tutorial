"""
Author: Ronald Munoz
Date: OCT/23/2021
""" 

# Import global resources
from sys import path
path.append(".")
import resources

# Display header
resources.displayLessonIntroMessage(1)

tObject = resources.TestBed()

"""
    Variables and Data Types
    En esta seccion vamos aplicar lo que hemor aprendido acerca de variables y datatypes.
"""
print("\n* Variables *\n")
# --------------------------------------------------------------- #
# 1. Declara una variable tipo integer llamada mi_integer
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_integer = 100

# print("El valor de mi_integer es = {} y es tipo {}".format(mi_integer, type(mi_integer)))

# --------------------------------------------------------------- #
# 2. Declara una variable tipo float llamada mi_float 
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_float = 2.8

# print("El valor de mi_float es = {} y es tipo {}".format(mi_float, type(mi_float)))

# --------------------------------------------------------------- #
# 3. Declara una variable tipo string llamada mi_string
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_string = "Hello World"

# print("El valor de mi_string es = {} y es tipo {}".format(mi_string, type(mi_string)))

# --------------------------------------------------------------- #
# 4. Declara una variable tipo boolean llamada mi_bool
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_bool = False

# print("El valor de mi_bool es = {} y es tipo {}".format(mi_bool, type(mi_bool)))

# --------------------------------------------------------------- #
# 5. Declara una variable tipo complex llamada mi_complex
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_complex = 1j

# print("El valor de mi_complex es = {} y es tipo {}".format(mi_complex, type(mi_complex)))

# --------------------------------------------------------------- #
# 6. Declara una variable tipo list llamada mi_list
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_list = [1,2,3,4,5]

# print("El valor de mi_list es = {} y es tipo {}".format(mi_list, type(mi_list)))

# --------------------------------------------------------------- #
# 7. Declara una variable tipo dict llamada mi_dict
# --------------------------------------------------------------- #
""" Escribe tu codigo despues de este comentario """
# mi_dict = {"llave":"valor"}

# print("El valor de mi_dict es = {} y es tipo {}".format(mi_dict, type(mi_dict)))



print("\n* Casting *\n")
"""
    Casting
    Elimina los comentarios de los siguientes fragmentos de codigo 
    y analiza el resultado. Intenta hacer esto un ejemplo a la vez
"""
# --------------------------------------------------------------- #
# 8. Puedes indicar tipo de las siguientes variables?
# --------------------------------------------------------------- #

# x = float(2)
# print("El valor de x es = {} y es tipo {}".format(x, type(x)))

# y = str(1000000.000000000)
# print("El valor de y es = {} y es tipo {}".format(y, type(y)))

# # Presta atencion en que esta pasa con el punto decimal
# z = str(1000000.0009)
# print("El valor de y es = {} y es tipo {}".format(y, type(y)))

# Que pasa cuando intentamos forzar un valor int a un str? (ERROR vuelve a comentar este fragmento)
# i = int('A')
# print("El valor de i es = {} y es tipo {}".format(i, type(i)))

# w = float("4.2")
# print("El valor de w es = {} y es tipo {}".format(w, type(w)))


tObject.printTestBedSummary()