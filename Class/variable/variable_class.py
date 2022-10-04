'''
  ****Type of varaible in Python****

  Instance varaible (Object lavel variable)
  Static variable (Class lavel variable)
  Local variable (Methode lavel variable)


'''

'''
   
    ****** Types of Method *****
    class  method
    Instance method
    static method

'''

'''
    The Way to create object in python class 

    object_name = className()

'''

class Student:
    def __init__(self):
        self.name = "neeraj"
        self.rollno = 1234
        self.marks = 85

    def talk(self):
        print("Hello i am" , self.name)
        print("My roll no", self.rollno)
        print("I have got marks", self.marks)

s = Student()
s.talk()
