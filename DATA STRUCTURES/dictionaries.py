# collection of key value pairs
point = {"x": 1, "y": 2}
points = dict(x=1, y=2)
points["x"] = 30
print(points)

points["z"] = 30
del points["z"]


# for x in range(5):
#     value.append(x * 2)
#     print(value)
values = [x*2 for x in range(5)]
print(values)
