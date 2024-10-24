class Circle:
    def __init__(self, radius):
        self.radius = radius
    def info(self):
        return f"Circle with radius {self.radius}"
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def info(self):
            return f"Rectangle with width {self.width} and height {self.height}"
        def display_info(shape):
            print(shape.info())        