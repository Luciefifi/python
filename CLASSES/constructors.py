# constructors
# self is a reference to the current object
# every object must have atleast one parameter which is by convetion self

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point( {self.x},{self.y} )")


point = Point(1, 2)
print(point.x)
point.draw()
