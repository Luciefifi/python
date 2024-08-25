class Point:

    default_color = "Red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point( {self.x},{self.y} )")
Point.default_color="Yellow"

point = Point(1, 2)
point.default_color="green"
point .default_color
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3,5)
another.draw()