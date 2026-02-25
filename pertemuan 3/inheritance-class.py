class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        

d1 = Dog("Rex")
d1.speak()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, tahun):
      super().__init__(fname, lname)
      self.tahunLulus = tahun
    def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.tahunLulus)

x = Student("John", "Doe", 2026)
x.printname()

