class Point:
    def __init__(self,x,y) :
        self . x = x
        self . y = y
    
    def __add__(self,other):
        return Point(self.x + other.x  , self.y + other.y)
        # return self.x + other.x  , self.y + other.y

point = Point(1,2)
other = Point(2,1)
combined = point + other
print(combined.x)
# print(point + other)