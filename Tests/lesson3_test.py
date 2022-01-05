"""
Author: Ronald Munoz
Date: DEC/22/2021
""" 
from sys import path
import pytest

# Import working file
path.append("./Lessons/Lesson3/.")

import Lesson3 as L3

test_func1_input_output_data = [
    (1, "1 \n"),
    (5, "1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n"),
    (10,"1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n1 2 3 4 5 6 \n1 2 3 4 5 6 7 \n1 2 3 4 5 6 7 8 \n1 2 3 4 5 6 7 8 9 \n1 2 3 4 5 6 7 8 9 10 \n"),
]

@pytest.mark.parametrize('sample, expected', test_func1_input_output_data)
def test_leap_year(sample, expected):
    assert L3.func1(sample) == expected


test_func2_input_output_data = [
    (2, "  1 \n 1 1 \n"),
    (5, "     1 \n    1 1 \n   1 2 1 \n  1 3 3 1 \n 1 4 6 4 1 \n"),
]

@pytest.mark.parametrize('sample, expected', test_func2_input_output_data)
def test_func2(sample, expected):
    assert L3.func2(sample) == expected

test_fibonacci_input_output_data = [
   (1,1),
   (7,13),
   (12,144)
]

@pytest.mark.parametrize('sample, expected', test_fibonacci_input_output_data)
def test_func3(sample, expected):
    assert L3.func3(sample) == expected
