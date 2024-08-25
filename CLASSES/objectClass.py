
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")



class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swimm")


m = Mammal()
print(isinstance(m,object))
print(issubclass(Mammal,object))
