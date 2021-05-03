
""" A platform for UMD I-School students to look up class prerequisites, plan 
    their schedules, and find contact information for advisors.
"""

class Student:
    """ An instance of a UMD Information Science student.

    Attributes:
        student_id (int): the unique identifying number of the student
        student_name (str): the name of the student
        grad_year (int): the intended graduation year of the student
    """
    
    def __init__(self, student_id, student_name, grad_year, classes_taken):
        """ Assigns attributes to objects, instantiates a student class

        Args:
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            grad_year (int): the intended graduation year of the student
            classes_taken (list of str) : the list of classes the student has
              taken 
        
        Side effects:
            creates global variables, specifically student_id, student_name, 
              grad_year, and classes_taken
        """
        self.student_name = student_name
        self.student_id = student_id
        self.grad_year = grad_year
        self.classes_taken = classes_taken


    def greet(self):
      """ This method takes a student's name and and student's identification 
      number to create a customized greeting based on the inputs of the student 
      trying to use our program.

      Args:
        self (Student) : an instance of the Student Class

      Returns: 
        welcome (str) : This method returns our welcome statements with the 
          student's name and identification number in the greeting.
      """
      welcome = input(f'Welcome, {self.student_name} (UID: {self.student_id}),'+
                    ' to I-School help! What can we assist you with? ' +
                    'Please choose from the following list of options: \n' +
                    'Benchmark I Classes \nBenchmark II Classes \nCore Courses'+
                    '\nMajor Specializations \nCredit Counter \nAdvising '+
                    'Contacts \nUpdate Classes Taken \nChange Name, Graduation'+
                    ' Year')
      return welcome
   

    def get_classes(self):
      """ This method uses a loop to allow students to enter the classes that 
      they have taken that are part of the Information Science major, stores 
      them in a list, and then returns the list with the classes in it. 

      Returns: 
        student_classes (list) : the inputted classes that the student has 
        taken in the Information Science major. 
      """
      count = 0
      self.classes_taken = []
      while count == 0:
        classes = input('Please enter your INST classes one at a time. ' +
                        'Enter stop when you have entered all your' + 
                        'classes.\n')
        if classes != "stop":
          self.classes_taken.append(classes)
        else:
          count += 1     
      return self.classes_taken


    def benchmark_I():
      """
      """
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
      """
      """
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
    
    
    def core_courses(taken):
      """Determines a list of core INST courses that the student must still
      take
        
      Args:
        taken (list): list of strings of INST classes that the student has 
            already received credit for
        
      Returns:
        a list of core INST courses
      """


    def specializations(specialization):
      """Finds all the classes in the specified specialization parameter
      
      Args:
        specialization (string): a string of the specialization (cybersecurity,
            data science, healthcare, digital curation)
        
      Returns:
        a list of courses in the specified information science specialization 
      """


    def credit_counter(classes_taken):
      """
      """
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
        """ This function will use imported modules to web scrape the UMD's
        School of Information's website so that we can retrieve data on request.

        Args: 
            url_input (str) : the address to the site where we will derive 
                information from
        
        Returns: the part of the website that is searched for 
        """
    

    def write_to_file(student):
      """
      """
      pass


def load_from_file(student_id):
  """
  """
  with open('Students/'+ student_id, 'r', encoding = 'utf-8') as f:
    for line in f:
      attributes = line.strip().split(',')
      student_name = attributes[0]
      grad_year = attributes[1]
      taken_classes = attributes[2:]
      class_instance = Student(student_id, student_name, grad_year, taken_classes)
      return class_instance
  

def main():
  """
  """
  while True:
    been_here = input('Hi! Have you been here before? \n')
    if been_here.lower() == 'no':
      student_name = input("Please enter your full name: ")
      student_id = input("Please enter your student ID number: ")
      grad_year = input('Please enter your expected graduation year:')
      classes_taken = []
      class_instance = Student(student_id, student_name, grad_year, classes_taken)
      class_instance.get_classes()
      break
    elif been_here.lower() == 'yes':
      student_id = input("Please enter your student ID number: ")
      class_instance = load_from_file(student_id)
      break
    else:
      print('Please enter yes or no')
  
  option = class_instance.greet()
  if option == "Benchmark I":
      print(class_instance.benchmark_I())  
  elif option == 'Benchmark II':
      print(class_instance.benchmark_II())
  elif option == "Core Courses":
      class_instance.get_classes()
      print("C") 
  elif option == "Specializations":
      class_instance.get_classes()
      print("S") 
  elif option == "Advising Contacts":
      print("A") 
  elif option == "Credit Counter":
      print('You have completed '+ str(credit_counter(get_classes())) + ' INST credits.')
  else:
      print("I'm sorry, we don't know how to help you with that.")


if __name__ == "__main__":
  main()