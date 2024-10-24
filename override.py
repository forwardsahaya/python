class Shape:
    def area(self):
        print("Calculating area")
class Circle(Shape):
    def area(self):
        print("Calculating  area of circle")

circle =Circle()
circle.area()        
