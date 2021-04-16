"""A platform for UMD students to look up prerequistes for classes
"""

class Benchmark_1:
  """Determines whether a student has met their Benchmark 1 requirement
  Attributes: 
    course (str): course id 
    grade (float): grade student receives 
  """
  def __init__(self, course, grade):
    """Assigning attributes to objects 
    Args: 
       course (str): course id 
       grade (float): grade student receives 
    """
    self.course = course
    self.grade = grade 
    
  def pass_fail (course, grade):
    """This function will determine whether the student has Pass/Failed the class 
    and adds the course to their audit/profile
    
    Args: 
      See __init__ method
    Returns: passed courses 
    """
 def credit_counter (course):
  """Counts credits student has passed and how many more they need
  
  Args: 
    course (str): course id 
  Returns: number of outstanding credits 
  """
