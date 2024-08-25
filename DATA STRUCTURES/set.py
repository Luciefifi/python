# collection with no duplicates
numbers = [1, 22, 33, 44, 5, 5, 44, 33]
uniques = set(numbers)
second = {1, 3, 4}
print(numbers)
print(uniques)
print(second)

union = uniques | second
print(union)
print(uniques & second)
print(uniques ^ second)
print(uniques & second)