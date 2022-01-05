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
   return_string = ""

   for i in range(1, num_l + 1):
      # Run inner loop i+1 times
      for j in range(1, i + 1):
         return_string += str(j) + " "

      return_string += "\n"

   return return_string


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
   return_string = ""
   c = 1
   for i in range(num_rows):

      # Print required spaces
      return_string += (" " * (num_rows - i))

      for k in range(i + 1):
         if k == 0 or i == 0:
            c = 1
         else:
            c = c * (i-k+1)/k
         
         return_string += (str(int(c))  + " ")

      return_string += "\n"

   return return_string


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
   fib = [None] * (n+1)

   fib[0] = 0
   fib[1] = 1
   
   for i in range(2, n+1):
      fib[i] = fib[i - 1] + fib[i - 2]

   return fib[n]



if __name__ == "__main__":
   # Display header
   resources.displayLessonIntroMessage(3)

   """
   Tests:
   ** No modifiques la siguiente seccion ** 
   """
   retcode = pytest.main(["-s", "Tests/lesson3_test.py"])
