import pytest
from umd_student_platform import Student
import builtins
from unittest import mock

def test_credit_counter():
    student1 = Student(115998247, 'Amelia Guenterberg', 2022, ['INST 201','INST 311','INST 409'])
    student2 = Student(222222222, 'Sally Smith', 2048, ['PSYC 100','INST 311','INST362','INST346'])
    assert student1.credit_counter() == 9
    assert student2.credit_counter() == 12


def test_get_classes():
    student1 = Student('112233445', 'Sally Smith', 2022, [])
    with mock.patch("builtins.input", side_effect = ['INST 201','INST 326','PSYC 100','MATH 115',"GEOG 130","ARTH 220",'stop',"INST 999"]):
        assert student1.get_classes() == ['INST 201','INST 326','PSYC 100','MATH 115']
        assert student1.classes_taken == ['INST 201','INST 326','PSYC 100','MATH 115']
