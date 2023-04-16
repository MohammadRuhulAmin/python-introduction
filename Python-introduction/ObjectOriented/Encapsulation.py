
class Circle:
    def __init__(self,radius,const):
        print('Constructor called!')
        # __variable is used for as a private variable!
        self.__radius = radius
        self.__const = const
    def set_radius(self, radius):
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_const(self,const):
        self.__const = const
    def get_const(self):
        return self.__const


radius = 123
const = 3.1416
c1 = Circle(radius,const)

print(c1.get_radius()*4*c1.get_radius()*c1.get_const())
c1.set_const(1)
c1.set_radius(2)
print(c1.get_radius()*4*c1.get_radius()* c1.get_const())