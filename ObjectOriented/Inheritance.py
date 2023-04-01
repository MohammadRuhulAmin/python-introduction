class Polygon:
    __height = None
    __width = None
    def set_values(self,widht,height):
        self.__width = widht
        self.__height = height
    # def __init__(self,width,height):
    #     self.__width = width
    #     self.__height = height
    def set_width(self,width):
        self.__width = width
    def get_width(self):
        return self.__width
    def set_height(self,height):
        self.__height = height
    def get_height(self):
        return self.__height
class Triangle(Polygon):
    def area(self):
        return self.get_width()* self.get_height() * 0.5

class Rectangle(Polygon):
    def area(self):
        return self.get_width() *self.get_height()

rec1 = Rectangle()
rec1.set_height(12)
rec1.set_width(10)
print(rec1.area())
tr1 = Triangle()
tr1.set_values(12,22)
print(tr1.area())



