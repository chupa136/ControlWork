#Задание 1
class Person:
    def __init__(self, age=0):  # age по умолчанию 0 (можно не передавать)
        self._age = age

    def set_age(self, age):
        if age <= 0:
            print("Ошибка! Возраст не может быть отрицательным или нулевым")
            return
        self._age = age

    def get_age(self):
        return self._age




p = Person()
p.set_age(25)
#print(p.get_age())  # 25
#p.set_age(-5)       #Ошибка


#Задание 2
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
         return f"I am an animal"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Meow"



dog = Dog("Buddy")
cat = Cat("Kitty")

#print(dog.name, dog.speak())    # Buddy Woof
#print(cat.name, cat.speak())    # Kitty Meow

#Задание 3

class Vehicle:
    def move(self):
        return 'Vechicle is moving'

class Car(Vehicle):
    def move(self):
        return 'Car is driving'

class Bicycle(Vehicle):
    def move(self):
        return 'Bicycle is pedaling'

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

#print(move(car))    #Car is driving
#print(move(bike))   #Bicycle is pedaling

#Задание 4

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        pi = 3.1415
        return pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())       # Вывод: 50
print(circle.area())     # Вывод: ~153.94


