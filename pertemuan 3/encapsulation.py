class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Properti Privat

  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("umur harus bernilai positif")

p1 = Person("Emil", 25)
print(p1.name)
print(p1.get_age())# cara mengakses properti privat

p1.set_age(26)# setting umur
print(p1.get_age())# menampilkan kembali umur yang sudah diubah


class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # ini akan menyebabkan error

