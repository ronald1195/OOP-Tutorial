"""
Author: Ronald Munoz
Date: DEC/07/2021
""" 
from sys import path
# Import global resources
path.append(".")
import resources

import pytest

"""
   For Loops
"""

def func1(num_l):
   """   
   Esta funcion debe de regresar un string que sea igual a:
   1 
   1 2 
   1 2 3 
   1 2 3 4 
   1 2 3 4 5

   usando loops. 

   Ya que este ejercicio es totalmente basado en strings voy a darte algunas pistas 
   de algunas cosas a las que tienes que prestar mucha atencion. 

   Si func() recibe 1 como un argumento entonces el string que esta funcion debe regresar
   se veria asi "1 \n"

   "\n" va a ser parte de cada una de las lineas generadas por esta funcion. Al mismo tiempo,
   cada numero ira seguido de un espacio " ".
   """
   pass


def func2(num_rows):
   """
   Esta funcion debe regresar un string con n numero de lineas
   representando el triengulo de pascal. 

   Ejemplo:
        1 
       1 1 
      1 2 1 
     1 3 3 1 
    1 4 6 4 1

   Para este ejercicio recuerda que los espacios importan, tanto antes como despues de 
   cada uno de los numeros. 

   Como referencia, la ultima linea del triangulo debe tener 1 espacio en blanco antes de la linea y 
   n espcios en la primera linea antes de el primer numero que se imprime. Lo mas importante
   aqui es recrear el algorithmo que genera el Triangulo de Pascal pero reproducir el formato 
   deseado no deberia de ser demasiado complicado de obtener. 

   Tu funcion va a ser probada en contra de varios test cases. 
   """
   pass


def func3(n):
   """
   FIBONACCI
   Los números Fibonacci son una secuencia de números definidos recursivamente 
   por la fórmula:

   F0 = 1 
   F1 = 1 
   Fn = Fn_2 + Fn_1 donde n ≥ 2. 

   Esto significa que cada término de la secuencia después de los dos primeros, 
   es la suma de los dos términos previos.

   Los primero numeros de esta secuencia son:
   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

   Esta funcion debe de aceptar un numero como argumento que simboliza el indice
   del numero de la secuencia de numeros fibonnaci que queremos regresar. 

   Ejemplo:
   func3(1) == 1
   func3(7) == 13
   """
   pass



if __name__ == "__main__":
   # Display header
   resources.displayLessonIntroMessage(3)

   """
   Tests:
   ** No modifiques la siguiente seccion ** 
   """
   retcode = pytest.main(["-s", "Tests/lesson3_test.py"])
