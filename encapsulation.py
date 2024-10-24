class Dog:
    def __init__(self, name, breed):
        self._name = name
        #protected attribute
        self._breed = breed
    def get_name(self):
        return self._name
    def set_name (self, name):
        self._name = name
        #Example of encapsulation

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.get_name())
#output buddy
my_dog.set_name("Max") 
print(my_dog.get_name())                
        