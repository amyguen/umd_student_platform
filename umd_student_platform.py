
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
        self.student_name = student_name
        self.student_id = student_id
        self.grad_year = grad_year

    def greet(student_id, student_name):
      """
      This function takes a student's name and and student's identification number to create a customized greeting based on the inputs of the student trying to use our program.

      Args:
        student_id (string): student's identification number
        student_name(string): students's full name 

      Returns: 
        welcome (string):This function returns our welcome statements with the student's name and identification number in the greeting. 

      """
   
      welcome = input('Welcome, ' + student_name +' (UID:) '+ student_id + ',to I-School help! What can we assist you with?' +
                    'Please choose from the following list of options:\n' +
                    'Benchmark I\nBenchmark II\nCore Courses\nSpecializations\n'+
                    'Advising Contacts\nCareer Advice\nCredit Counter\n')
      return welcome
   
    def get_classes():
      """
      This function uses a loop to allow students to enter the classes that 
      they have taken that are part of the Information Science major, stores 
      them in a list, and then returns the list with the classes in it. 

      Args:
        This function has no set arguments. 

      Returns: 
        student_classes(list): the inputted classes that the student has 
        taken in the Information Science major. 

      """
      count = 0
      student_classes = []
        
      while count == 0:
        classes = input('Please enter your INST classes one at a time.' +
                        'Enter stop when you have entered all your' + 
                        'classes.\n')
        if classes != "stop":
          student_classes.append(classes)
        else:
          count += 1
                
      return student_classes

    def benchmark_I():
      
      
      requirements = input('Have you taken MATH115 or higher and psych100? ')
      if requirements == 'no':
          incomplete = 'You have not completed the benchmark I courses.'
          return incomplete
      elif requirements == 'yes':
          completed = 'You have completed the benchmark I courses.'
          return completed
      else:
          response = 'Please try again and enter either yes or no.'
          return response
      
    def benchmark_II():
      
      requirements = input('Have you taken STAT100, INST126, and INST201? ')
      if requirements == 'no':
          incomplete = 'You have not completed the benchmark II courses.'
          return incomplete
      elif requirements == 'yes':
          completed = 'You have completed the benchmark II courses.'
          return completed
      else:
          response = 'Please try again and enter either yes or no.'
          return response
          
    def credit_counter(classes_taken):
      credits = len(classes_taken) * 3
      return credits
      
  

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
      
      student_name = input("Please enter your full name: ")
      student_id = input("Please enter your student ID number: ")
      
      option = greet(student_id, student_name)
      
      if option == "Benchmark I":
          print(benchmark_I())
          
      elif option == 'Benchmark II':
          print(benchmark_II())
      
      elif option == "Core Courses":
          get_classes()
          print("C")
          
      elif option == "Specializations":
          get_classes()
          print("S")
          
      elif option == "Advising Contacts":
          print("A")
          
      elif option == "Credit Counter":
          print('You have completed '+ str(credit_counter(get_classes())) + ' INST credits.')

      else:
          print("I'm sorry, we don't know how to help you with that.")

if __name__ == "__main__":