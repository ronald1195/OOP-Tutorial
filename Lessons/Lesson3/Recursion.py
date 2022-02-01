"""
Author: Ronald Munoz
Date: JAN/31/2022
""" 
from sys import path
# Import global resources
path.append(".")
import resources

import pytest

"""
   Recursion
"""

def rec1():
    """Que se necesita para que este if statement regrese "Correcto"?"""
    flag = 0

    if flag:
        return "Correcto"
    else:
        return "Incorrecto"


if __name__ == "__main__":
   # Display header
   resources.displayLessonIntroMessage(11) # Special Topic Header

   """
   Tests:
   ** No modifiques la siguiente seccion ** 
   """
   retcode = pytest.main(["-s", "Tests/recursion_test.py"])