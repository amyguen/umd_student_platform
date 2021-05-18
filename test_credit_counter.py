import pytest
import umd_student_platform as u

student = u.Student(554433221, 'Michael Rush', 2022, ['INST 201'])

def test_credit_counter():
    #testing "credit_counter()""
    assert isclose(student.credit_counter(), 3)
