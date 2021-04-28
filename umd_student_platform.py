
""" A platform for UMD I-School students to look up class prerequisites, plan 
    their schedules, find contact information for advisors, and view potential
    career options.
"""
def greet(student_id, student_name):
    welcome = input('Welcome to I-School help! What can we assist you with?')
    if welcome == 'Benchmark Classes':

    elif welcome == 'Core Courses':
        
    elif welcome == 'Specializations':
        
    elif welcome == 'Advising Contacts':
        
    elif welcome == 'Career Advise':
        
    elif welcome == 'Credit Counter':

    else:
        wrong_input = input("I'm sorry, we don't know how to help you with that. Please choose another option.")



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
        self.student_name = student_name
        self.student_id = student_id
        self.grad_year = grad_year


    def benchmark_I(student_id, student_name, completed):
        """Determines whether a student has met their Benchmark 1 requirement
        Args: 
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            completed (list of str): a list of courses the student has already
                received credit for
            
    """
        class_list = ['in here we will put the benchmark I classes']
        print('These are the Benchmark I classes for the I-School:')
        print(class_list)
        classes_taken = input('Which of these have you taken?')


    def benchmark_II(student_id, student_name, completed):
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

    def data_retrieval(url_input):
        """
        This function will use imported modules to web scrape the UMD's
        School of Information's website so that we can retrieve data on request.

        Args: 
            (string)url: the address to the site where we will derive 
                information from
        
        Returns: the part of the website that is searched for 
        """
    
    def career_opportunities(career_preferences):
        """
        This function returns the opportunities available based on a particular
        career input by the user. This function might scrape a website that 
        provides specific jobs available. 

        Args: 
            career_preferences(string): the input put in by the user. We will 
                probably provide options for the career preferences that can be chosen.
        
        Returns: 
            opportunities(string): jobs available based on the input.

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
    
    def benchmark_I(student_id, student_name, completed):
        """Determines whether a student has met their Benchmark 1 requirement
        Args: 
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            completed (list of str): a list of courses the student has already
                received credit for
            
    """
      
        
    
    def pass_fail(course, grade):
        """This function will determine whether the student has Pass/Failed the class 
        and adds the course to their audit/profile
        
        Args:
            course (str) : the course the student inputs
            grade (str) : the grade received in the course
        Returns: 
            passed courses 
    """
    def credit_counter(course):
        """Counts credits student has passed and how many more they need
        
        Args: 
            course (str): course id 
    
    Returns: number of outstanding credits 
  """
def main():
    

 if __name__ = "__main__":