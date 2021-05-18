import pytest 
from umd_student_platform import Student



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


    
