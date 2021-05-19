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

def test_benchmark1(capsys):
    """Does benchmark_1 print out the correct print statement? """
    student_1 = Student('114007245','Mario Castillo',2018, ["INST 201","INST 326"])
    student_2 = Student('117006012', 'Joe Rogan', 2018, ["MATH 115","PSYC 100"])
    student_3 = Student("117008490", "Kanye West", 2018, ["MATH 120","STAT 003"])
    student_4 = Student('118009044', "Elon Musk", 2018, ["PSYC 100","MATH 003"])
    
    student_1.benchmark_I()
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == ('You have not completed the Benchmark I requirements.\n'
    'You have not taken MATH 115 or higher.\n'
    'You have not taken PSYC 100.\n')

    student_2.benchmark_I()
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == (f'You have completed all of your Benchmark I courses! '
    f'Congratulations, {student_2.student_name}!\n')

    student_3.benchmark_I()
    outerr = capsys.readouterr()
    out = outerr.out 
    assert out == ('You have not completed the Benchmark I requirements.\n'
    'You have not taken PSYC 100.\n')

    student_4.benchmark_I()
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == ('You have not completed the Benchmark I requirements.\n'
    'You have not taken MATH 115 or higher.\n')

def test_advising():
    student_1 = Student('114007245','Mario Castillo',2018, ["INST 201","INST 326"])
    out = student_1.resources()
    assert out == ("Hi Mario Castillo, the following resources can help you to prepare for the courses" 
            "you will be taking in the InfoSci program.\n"
            "\nPython:\n"
            "\n\t Essential Python Topics:"
            "\n\t\t -Statements, variables, basic data types & operators"
            "\n\t\t -Conditional statements"
            "\n\t\t -Loops"
            "\n\t\t -Lists, dictionaries, tuples"
            "\n\t\t -Input and output"
            "\n\t\t -Reading and writing files"
            "\n\t\t -Functions, libraries, modules"
            "\n\t\t -Testing & debugging"
            "\n\n\t Python Books"
            "\n\t\t -Python for Everybody - $10 print, free online"
            "\n\t\t -Python Crash Course - $40 print, $32 ebook"
            "\n\t\t -CS Principles: Big Ideas in Programming - free, with" 
            "interactive examples"
            "\n\n\t Online Python Courses and Tutorials"
            "\n\t\t -Codecademy Python - free"
            "\n\t\t -The Python Guru - free"
            "\n\t\t -DataCamp Python Programming courses - Intro course free; others charged by the month"
            "\n\t\t -Coursera - These can be audited for free. If you pay, you can get feedback and \"grades\":"
            "\n\t\t -http://pythontutor.org - free"
            "\n\t\t -https://stackoverflow.com - free" 
            "\n\t\t -w3schools.com - free "
            "\n\t\t -Corry Schafer Youtube Channel - free "
            "\nR:\n"
            "\n\t “-Statistics (The Easier Way) with R: an informal text on applied statistics” by N.M. Radziwill ISBN13 - 9780996916059"
            "\n\t -Datacamp.com"
            "\n\t -Codecademy.com\n")
    
test_advising()