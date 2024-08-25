# inheritance prevent codes duplication and allows us to reuse codes

class Animal:
    def eat(self):
        print("Eat")


class Bird(Animal):
    def fly(self):
        print("Fly")

class Chicken(Bird):
    pass
   