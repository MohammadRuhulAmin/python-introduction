
class Polygon:
    def __init__(self,name):
        print(name)

class Triangle(Polygon):
    def __init__(self):
        print('Triangle Constructor called')
        super().__init__('Ruhul Amin')


tr1 = Triangle()
# className.__mro__
#mro stands for mathod resolution order!
print(Triangle.__mro__)