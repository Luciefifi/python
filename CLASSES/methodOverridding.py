# methos overridding: replacong or extending the methos defined in the base class

class Animal:
    def __init__(self):
        print("Animal ocnstructor")
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
     def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight = 2

     def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swimm")


m = Mammal()
print(m.age)
print(m.weight)
