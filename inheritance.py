#parent class
class Animal:
    def _init_(self, name):
        self.name = name
    def make_sound(self):
        return "Some sound"  
# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} is barking!"
#Example of inheritance 
my_dog = Dog("Buddy")
print(my_dog.make_sound())