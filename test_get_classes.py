import pytest
import builtins
from unittest import mock
from umd_student_platform import Student

def test_get_classes():
    student1 = Student('112233445', 'Sally Smith', 2022, [])
    with mock.patch("builtins.input", side_effect = ['INST 201','INST 326','PSYC 100','MATH 115',"GEOG 130","ARTH 220",'stop',"INST 999"]):
        assert student1.get_classes() == ['INST 201','INST 326','PSYC 100','MATH 115']
        assert student1.classes_taken == ['INST 201','INST 326','PSYC 100','MATH 115']

# def test_get_user_info():
#     """Does get_user_info() return the user's name and age as a tuple?"""
#     with mock.patch("builtins.input", side_effect=["Alice", "27"]):
#         assert myproject.get_user_info() == ("Alice", 27)