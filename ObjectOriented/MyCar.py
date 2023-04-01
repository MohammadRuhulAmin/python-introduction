
class Car:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
        print(speed," => ",color)
        print("This is a constructor!~it is called first!")

ford = Car(12,'red')
audi = Car(12,'blus')
honda = Car(45,'gray')

ford.speed = 150
audi.speed = 200
honda.speed = 133

ford.color = 'blue'
audi.color = 'Green'
honda.color = 'red'

print(ford.speed)
print(audi.color)

class Rectangle:
    def __init__(self,height,width):
        self.height  = height
        self.width = width



rec1 = Rectangle(100,23)

print(rec1.height*rec1.width)
