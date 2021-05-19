
""" A platform for UMD I-School students to implement to help plan their class
schedules. """

import re

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

      Returns: 
        welcome (str) : This method returns our welcome statements with the 
          student's name and identification number in the greeting.
      """
      welcome = input(f'Welcome, {self.student_name} (UID: {self.student_id}),'+
                    ' to I-School help! What can we assist you with? ' +
                    'Please choose from the following list of options: \n\n' +
                    'Benchmark I \nBenchmark II \nCore Courses'+
                    '\nMajor Specializations \nCredit Counter \n'+
                    'Update Classes Taken \nChange Name or '+
                    'Graduation Year\nResources\nContact iSchool\n\n' + 
                    'Graduation Year\n\n' + 
                    'To choose an option, type the option how it is written ' +
                    'above. \n\nEnter quit to exit I-School help.\n\n\n')
      return welcome
   

    def get_classes(self):
      """ This method uses a loop to allow students to enter the classes that 
      they have taken that are part of the Information Science major, stores 
      them in a list, and then returns the list with the classes in it. 

      Returns: 
        student_classes (list) : the inputted classes that the student has 
        taken in the Information Science major. 
        
      Side Effects:
        changes the classes in the Student object
      """
      count = 0
      self.classes_taken = []
      class_options = r"^(MATH|STAT|PSYC|INST)\s{1}\d{3}"
      while count == 0:
        classes = input("Please enter all of the INST-related classes that " +
                  "you have taken, one at a time, in the following format:\n" +
                  "CLAS 100 \n For example, INST 201.\n\n Enter stop when you" +
                  " have finished. Don't forget to include I-School major " +
                  "benchmarks, like math and psychology courses! Thank you! \n")
          
        if classes.lower() != "stop":
          if not re.search(class_options, classes):
            print("Not a valid class")
          else:
            self.classes_taken.append(classes)
        else: 
          count += 1     
      return self.classes_taken


    def benchmark_I(self):
      """This function checks to see if the user has completed all
      benchmark I courses.

      Returns:
        new line (this was so our method would not return None)
       
      Side Effects:
        prints message onto the console
      """
      math_flag = False
      psych_flag = True
      for classes in self.classes_taken:
        split = classes.split()
        if split[0] == 'MATH':
          if int(split[1]) >= 115:
            math_flag = True
        
      if 'PSYC 100' not in self.classes_taken:
        psych_flag = False

      if math_flag and psych_flag:
          print(f'You have completed all of your Benchmark I courses! ' +
                f'Congratulations, {self.student_name}!')
      else:
        print('You have not completed the Benchmark I requirements.')
        if math_flag == False:
          print('You have not taken MATH 115 or higher.')
        if psych_flag == False:
          print('You have not taken PSYC 100.')
          
      return "\n"


    def benchmark_II(self):
      """This function checks to see if the user has completed 
      benchmark II courses based on input. If all three 
      courses satisfy our condition then you will have 
      completed benchmark II, if not our code will print 
      specific statements based on what the user has 
      completed.

       Returns:
        new line (this was so our method would not return None)

      Side effects: 
        prints message onto the console
      """
      stat_flag = True
      inst126_flag = True
      inst201_flag = True

      if 'STAT 100' not in self.classes_taken:
        stat_flag = False
      if 'INST 126' not in self.classes_taken:
        inst126_flag = False
      if 'INST 201' not in self.classes_taken:
        inst201_flag = False

      if stat_flag and inst126_flag and inst201_flag:
        print(f'You have completed all of your Benchmark II courses! ' +
              f'Congratulations, {self.student_name}!')
      else:
        print('You have not completed the Benchmark II requirements.')
        if stat_flag == False:
          print('You have not taken STAT 100. ')
        if inst126_flag == False:
          print('You have not taken INST 126. ')
        if inst201_flag == False:
          print('You have not taken INST 201. ')

      return "\n"
  

    def core_courses(self):
      """Checks to see if the student has completed all core courses.
      
       Returns:
        new line (this was so our method would not return None)
      
      Side Effects:
        prints a message onto the console 
      """
      core_courses = {'INST 311': True, 'INST 314': True, 'INST 326': True, 
                      'INST 327': True, 'INST 335': True, 'INST 346': True, 
                      'INST 352': True, 'INST 362': True}
      
      if 'INST 311' not in self.classes_taken:
        core_courses['INST 311'] = False
      if 'INST 314' not in self.classes_taken:
        core_courses['INST 314'] = False
      if 'INST 326' not in self.classes_taken:
        core_courses['INST 326'] = False
      if 'INST 327' not in self.classes_taken:
        core_courses['INST 327'] = False
      if 'INST 335' not in self.classes_taken:
        core_courses['INST 335'] = False
      if 'INST 346' not in self.classes_taken:
        core_courses['INST 346'] = False
      if 'INST 352' not in self.classes_taken:
        core_courses['INST 352'] = False
      if 'INST 362' not in self.classes_taken:
        core_courses['INST 362'] = False
        
      not_taken = []
      for course in core_courses:
        if core_courses[course] == False:
          not_taken.append(course)
          
      if len(not_taken) == 0:
        print("You have completed all core courses!")
      else:
        print("You must still complete the following core courses: ")
        print(*not_taken, sep = '\n')
        
      return "\n"


    def specializations(self):
      """Checks based on what specialization the student wants to complete, 
      which classes they still must complete or notifies them that they already
      completed that specialization's classes
      
      Side Effects:
        prints message onto the console
      """
      cyber_and_priv = {'INST364': True, 'INST365': True, 'INST366': True}
      choose_two = {'INST464': True, 'INST466': True, 'INST467': True}
      
      data_science = {'INST354': True, 'INST377': True, 'INST414': True,
                      'INST447': True, 'INST462': True}
      
      digital_cur = {'INST341': True, 'INST441': True, 'INST442': True,
                     'INST443': True, 'INST448': True}
      
      special = input("Which specialization are you interested in seeing the " 
                      + "requirements for? \nPlease choose from the " 
                      + "following list:\nCybersecurty and Privacy\n" 
                      + "Data Science\nDigital Curation\n")
      classes = {}
      
      if special != 'Cybersecurity and Privacy' and special != 'Data Science' and special != 'Digital Curation':
        print("Your selection was not listed. Please try again.")
   
      elif special == 'Cybersecurity and Privacy':
        if 'INST 364' not in self.classes_taken:
          cyber_and_priv['INST364'] = False
        if 'INST 365' not in self.classes_taken:
          cyber_and_priv['INST365'] = False
        if 'INST 366' not in self.classes_taken:
          cyber_and_priv['INST366'] = False
          
        count = 3
        if 'INST 464' not in self.classes_taken:
          choose_two['INST464'] = False
          count -=1
        if 'INST 466' not in self.classes_taken:
          choose_two['INST466'] = False
          count -=1
        if 'INST 467' not in self.classes_taken:
          choose_two['INST 467'] = False
          count -=1
        
        classes = cyber_and_priv
        not_taken = []
        for course in classes:
          if classes[course] == False:
            not_taken.append(course)
          
        if len(not_taken) == 0:
          if count >= 2:
            print("You have completed all the required cybersecurity and " + 
                  "privacy specialization courses!")
          else:
            print("You must complete two classes from these three options: " +
                  "INST464, INST466, INST467")
        else:
          print("You must still complete the following courses: ")
          print(*not_taken, sep = '\n')
        
      elif special == 'Data Science':
        if 'INST 354' not in self.classes_taken:
          data_science['INST354'] = False
        if 'INST 377' not in self.classes_taken:
          data_science['INST377'] = False
        if 'INST 414' not in self.classes_taken:
          data_science['INST414'] = False
        if 'INST 447' not in self.classes_taken:
          data_science['INST447'] = False
        if 'INST 462' not in self.classes_taken:
          data_science['INST462'] = False
          
        classes = data_science
        not_taken = []
        for course in classes:
          if classes[course] == False:
            not_taken.append(course)
          
        if len(not_taken) == 0:
          print("You have completed all the required data science courses!")
        else:
          print("You must still complete the following courses: ")
          print(*not_taken, sep = '\n')
          
      elif special == 'Digital Curation':
        if 'INST 341' not in self.classes_taken:
          digital_cur['INST341'] = False
        if 'INST 441' not in self.classes_taken:
          digital_cur['INST441'] = False
        if 'INST 442' not in self.classes_taken:
          digital_cur['INST442'] = False
        if 'INST 443' not in self.classes_taken:
          digital_cur['INST443'] = False
        if 'INST 448' not in self.classes_taken:
          digital_cur['INST448'] = False
        
        classes = digital_cur
        not_taken = []
        for course in classes:
          if classes[course] == False:
            not_taken.append(course)
          
        if len(not_taken) == 0:
          print("You have completed all the required digital curation courses!")
        else:
          print("You must still complete the following courses: ")
          print(*not_taken, sep = '\n')


    def credit_counter(self):
      """ Calculates the number of INST course credits that the student
      has accumulated for major requirements
      
      Returns:
        credits (int): the number of credits 
      
      Raises:
        ValueError: if the student has not taken any classes
      """
      credits = len(self.classes_taken) * 3
      if self.classes_taken == []:
        raise ValueError('Return to the beginning and input your classes taken.')
      else:
        return credits
      
    def resources(self):
      """This method prints some of the resources information that's listed under
      the InfoScience program structure page.

      Side effects:
        No side effects
      """
      
      return (f"Hi {self.student_name}, the following resources can help you to prepare for the courses" 
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
            "\n\t -Codecademy.com\n"         
      )
    def advising(self):
      
      """This method prints some of the information on the iSchool advising page

      Side effects:
        No side effects
      """
      
      return (f"Hi {self.student_name}, Advising information is printed below \n\nMain Office\n" 
            "-----------\n"
            "\nUniversity of Maryland"
            "\nCollege of Information Studies"
            "\n4130 Campus Drive"
            "\nHornbake Library, Ground Floor, Rm. 0220 "
            "\nCollege Park, MD 20742-4345"
            "\n(301) 405-2039"
            "\nHours: Mon-Fri, 9am-4pm"
            "\n\n\nDean’s Office\n"
            "-----------\n"
            "\nUniversity of Maryland"
            "\nCollege of Information Studies"
            "\n4161 Fieldhouse Drive"
            "\nPatuxent Building, Rm. 1117"
            "\nCollege Park, MD 20742-4911" 
            "\nHours: Temporarily Closed\n"
            "\nStudent Services & Program Teams\n"
            "-----------\n"
           "\nGeneral Inquiries: infosci@umd.edu"
           "\nAdvising: Virtual Advising" 
           "\nProgram Director: Vedat Diker, vdiker@umd.edu"
           "\nInterim Director for Undergraduate Operations: Ron Padron, rapadron@umd.edu\n"        
      )

    def update_classes(self):
      """ This method updates the list of classes a student has taken.

      Side effects:
        changes/adds classes to the Student object 
        prints an error if the class is already in their classes_taken attribute
      """
      flag = True
      class_options = r"^(MATH|STAT|PSYC|INST)\s{1}\d{3}"

      while flag:
        update = input('Thank you for updating your classes taken! This will '+
                    ' help us help you! \n Like before, please enter all of the '+
                    'INST-related classes that you have taken, one at a time, ' +
                    'in the following format: CLAS 100 \n For example, ' +
                    "INST 201.\n\n Enter stop when you have finished. Don't " +
                    'forget to include I-School major benchmarks, like math and' +
                    " psychology courses! Thank you! \n")
        if update.lower() != "stop":
          if not re.search(class_options, update):
            print("Not a valid class")
          else:
            if self.exists(update):
              print("According to our documentation, you've already taken this class.")
            else:
              self.classes_taken.append(update)
              self.add_new_classes_to_text(update)
        else: 
          flag = False


    def exists(self, str):
      """Assists the update_classes method by reading the unique student file

      Returns:
        True if the file can be opened and read, False otherwise
      """
      with open('Students/'+ self.student_id, 'r', encoding = 'utf-8') as f:
        if str in f.read():
          return True
        else:
          return False


    def add_new_classes_to_text(self, c):
      """Opens a file to be appended for the update_classes method
      
      Side effects:
        writing new classes to a student file
      """
      f = open('Students/'+ self.student_id, 'a', encoding = 'utf-8')
      c = "," + c
      f.write(c)


    def change_name_gradyear(self):
      """This method allows a student to update their name, graduation year, or
        both
      
      Side effects:
        writing the new name or graduation year to the student file
        prints an error if the user did not pick a valid option
      """
      running_flag = True
      while running_flag:
        options = input('Here, you can change your name and your expected ' +
                  'graduation year. \nTo update your name, type name. To update' 
                  + ' your graduation year, type grad year. To update both, ' +
                  'type both. Thank you! \n')
        if options.lower() == 'name':
          new_name = input("Please enter your full name: ")
          self.student_name = new_name
          self.write_to_file()
          running_flag = False
        elif options.lower() == 'grad year':
          new_grad_year = input('Please enter your updated graduation year: ')
          self.grad_year = new_grad_year
          self.write_to_file()
          running_flag = False
        elif options.lower() == 'both':
          new_name = input("Please enter your full name: ")
          new_grad_year = input('Please enter your updated graduation year: ')
          self.grad_year = new_grad_year
          self.student_name = new_name
          self.write_to_file()
          running_flag = False
        else:
          print("I'm sorry, you didn't pick a valid option")
          running_flag = True


    def write_to_file(self):
      """ Either creates or opens and writes new information to a student file,
        depending on which method write_to_file is called in (either main or
        change_name_gradyear)

        Side effects:
          creates and writes in a new file
          overwrites old information from an already existing file
      """
      with open('Students/'+ self.student_id, 'w+', encoding = 'utf-8') as f:
        class_list = ','.join(self.classes_taken)
        new_file = self.student_name + ',' + self.grad_year + ',' + class_list
        f.write(new_file)


def load_from_file(student_id):
  """Retrieves information from an already existing file and instantiates a 
    Student class

  Returns:
  class_instance (Student): a instantiation of the class Student
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
  """Runs the umd_student_platform program by greeting and determing what
  the student wants to do and executes that command

  Side effects:
    prints errors to the console when the user does not pick valid options
  """
  while True:

    been_here = input('Hi! Welcome to the UMD I-School Student Platform!\n' +
                    'Have you been here before? \n')
    if been_here.lower() == 'no':
      student_name = input("Please enter your full name: ")
      student_id = input("Please enter your 9 digit student ID number: ")
      grad_year = input('Please enter your expected graduation year: ')
      classes_taken = []
      class_instance = Student(student_id, student_name, grad_year, classes_taken)
      class_instance.get_classes()
      class_instance.write_to_file() 
      break

    elif been_here.lower() == 'yes':
      student_id = input("Please enter your 9 digit student ID number:  ")
      class_instance = load_from_file(student_id)
      break
    else:
      print('Please enter yes or no')
  
  option = class_instance.greet()
    
  if option == "Benchmark I":
      print(class_instance.benchmark_I()) 
  elif option == 'Benchmark II':
      print(class_instance.benchmark_II())
  elif option == 'Update Classes Taken':
    print(class_instance.update_classes())
  elif option == 'Change Name or Graduation Year':
      print(class_instance.change_name_gradyear())
  elif option == "Core Courses":
      print(class_instance.core_courses())
  elif option == "Major Specializations":
      print(class_instance.specializations())
  elif option == "Contact iSchool":
      class_instance.advising()
  elif option == "Credit Counter":
      print('You have completed '+ str(class_instance.credit_counter()) + 
              ' INST-related credits.')
  elif option == "Resources":
      class_instance.resources()
  elif option == "Credit Counter":
      print('You have completed '+ str(class_instance.credit_counter()) + 
              ' INST-related credits.')
  elif option == 'quit':
    print("Thank you for using this platform! Goodbye!")
  else:
      print("I'm sorry, we don't know how to help you with that.")

  while option != 'quit':
    option = class_instance.greet()

    if option == "Benchmark I":
        print(class_instance.benchmark_I()) 
    elif option == 'Benchmark II':
        print(class_instance.benchmark_II())
    elif option == 'Update Classes Taken':
      print(class_instance.update_classes())
    elif option == 'Change Name or Graduation Year':
        print(class_instance.change_name_gradyear())
    elif option == "Core Courses":
        print(class_instance.core_courses())
    elif option == "Resources":
        print(class_instance.resources())
    elif option == "Contact iSchool":
        print(class_instance.advising())
    elif option == "Major Specializations":
        print(class_instance.specializations())
    elif option == "Credit Counter":
        print('You have completed '+ str(class_instance.credit_counter()) + 
                ' INST credits.')
    elif option == "quit":
      print("Thank you for using this platform! Goodbye!")
    else:
        print("I'm sorry, we don't know how to help you with that.")


if __name__ == "__main__":
  main()