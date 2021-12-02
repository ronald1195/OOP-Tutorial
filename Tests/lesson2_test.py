"""
Author: Ronald Munoz
Date: NOV/24/2021
""" 
from sys import path
import pytest

# Import working file
path.append("./Lessons/Lesson2/.")
# from Lesson2 import func1, func2

import Lesson2 as L2

"""
    Lesson 2 Tests
"""

def test_func1():
    assert L2.func1() == "Correcto"

def test_func2():
    assert L2.func2() == "Correcto"

test_three_input_output_data = [
    (99, "A+"),
    (90, "A"),
    (85, "B+"),
    (81, "B"),
    (82, "B-"),
    (77, "C+"),
    (76, "C"),
    (70, "C-"),
    (67, "D+"),
    (63, "D"),
    (60, "D-"),
    (0, "F"),
    (59, "F"),
    (93.2, "Error"),    # Floats not allowed
    (101, "Error"),     # Larger values not allowed
    (-20, "Error")      # Negative numbers not allowed
]

@pytest.mark.parametrize('sample, expected', test_three_input_output_data)
def test_score_conversion(sample, expected):

    assert L2.transformar_puntos_a_calificacion(sample) == expected