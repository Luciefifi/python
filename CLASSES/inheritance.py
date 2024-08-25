# inheritance is a mechanism that allows us to define the common behavior or common functions in one class that are inheritad in another classes

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")
# Animal : Parent,base class
# Mammal" child,sub class


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swimm")


m = Mammal()
m.eat()
print(m.age)
