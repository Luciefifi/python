# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


point1 = Point(x=1, y=2)
point2 = Point(x=1, y=2)
print(point1 == point2)
