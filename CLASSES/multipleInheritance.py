# class with multiple base classe

# class Employee:
#     def greet(self):
#         print("Employee greet")


# class Person:
#     def greet(self):
#         print("Person greet")


# class Manager(Employee, Person):
#     pass

# manager = Manager()
# manager.greet()


class Flyer:
    def fyl(self):
        pass


class Swimmer:
    def swimm(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
