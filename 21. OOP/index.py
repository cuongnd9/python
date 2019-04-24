class Animal:
  def sayHi(self):
    print('Hiiiiiiiiiiiiiiiiiiiiii')


class Cat(Animal):

  name = 'Meowwwwwwww'

  def __init__(self, color = 'white', age = 1):
    self.color = color
    self.age = age
  
  def getColor(self):
    print(self.color)


print(Cat.name)

dog = Cat()
dog.sayHi()
dog.getColor()
