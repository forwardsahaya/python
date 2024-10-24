#class and object creation
class car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f'model: {self.model}, color: {self.color}')

carl = car("Toyota", "Red")
carl.display_info()            