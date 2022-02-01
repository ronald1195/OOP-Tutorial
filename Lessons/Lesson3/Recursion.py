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

def fibonacci_recursive(n):
    """
    """
    pass

def factorial_recursive(n):
    """
    """
    pass


if __name__ == "__main__":
   # Display header
   resources.displayLessonIntroMessage(11) # Special Topic Header

   """
   Tests:
   ** No modifiques la siguiente seccion ** 
   """
   retcode = pytest.main(["-s", "Tests/recursion_test.py"])