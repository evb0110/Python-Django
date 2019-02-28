class Dog:
  def __init__(self, name, age, furcolor = "black"):
    self.name = name
    self.age = age
    self.furcolor = furcolor

  def bark(self):
    print("BARK!")

mydog = Dog("John", 13)

print(mydog.name, mydog.furcolor)
