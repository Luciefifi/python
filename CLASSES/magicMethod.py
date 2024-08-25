
# magic methods: methods that have two unde3rscores at the beginning and at the end of the name and they called aoutomatically when you create a new object

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self, x, y):
        print(f"point ({x},{y})")


point = Point(1, 2)
print(point)
