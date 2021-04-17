
""" A platform for UMD I-School students to look up class prerequisites, plan 
    their schedules, find contact information for advisors, and view potential
    career options.
"""

class Student:
    """ An instance of a UMD Information Science student.

    Attributes:
        student_id (int): the unique identifying number of the student
        student_name (str): the name of the student
        grad_year (int): the intended graduation year of the student
    """
    
    def __intit__(self, student_id, student_name, grad_year):
        """ Assigns attributes to objects, instantiates a student class

        Args:
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            grad_year (int): the intended graduation year of the student
        
        Side effects:
            creates global variables, specifically student_id, student_name, and
                grad_year
        """
    

    def benchmark_2(student_id, student_name, completed):
        """ Returns to the student a list of Benchmark II courses in the 
            Information Science department, returns to the student prerequisites 
            for any inputted Benchmark II class, returns Benchmark II classes 
            the student has yet to fulfill.

        Args:
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            completed (list of str): a list of courses the student has already
                received credit for

        Returns:
            list: a list of Benchmark II classes within the Information Science
                department
            list: a list of prerequisites for an inputted Benchmark II class
            list: a list of Benchmark II classes the student has yet to fulfill
        
        Raises:
            ValueError: student did not input a valid Benchmark II class
        """
    

    def advising_contacts(student_id, student_name, specialization):
        """ Returns to the student a list of advisors and their contact 
            information that are best recommended to the student based on their 
            specialization.

        Args:
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            specialization (str): optional, the name of the specialization of 
                the student, default none
        
        Returns:
            list: the name and contact information of advisors that are best
                recommended for the student
        """
    
    def specializations(specialization):
      """Finds all the classes in the specified specialization parameter
      
      Args:
        specialization (string): a string of the specialization (cybersecurity,
        data science, healthcare, digital curation)
        
      Returns:
        a list of courses in the specified information science specialization 
      """
      
    def core_courses(taken):
      """Determines a list of core INST courses that the student must still
      take
        
      Args:
        taken (list): list of strings of INST classes that the student has 
        already received credit for
        
      Returns:
        a list of core INST courses
      """
      
    if __name__ = "__main__":
        
      
        


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
    
  def pass_fail(course, grade):
    """This function will determine whether the student has Pass/Failed the class 
    and adds the course to their audit/profile
    
    Args: 
    See __init__ method
    Returns: passed courses 
    """
 def credit_counter(course):
  """Counts credits student has passed and how many more they need
  
  Args: 
    course (str): course id 
    Returns: number of outstanding credits 
  """