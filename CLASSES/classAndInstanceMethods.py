class Point:

    default_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"point( {self.x},{self.y} )")


point = Point(0,0)
point =point.zero()
point.draw()
