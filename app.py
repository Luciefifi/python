# # print("Hello world🙌")
# import math

# # # multiplying the asteris 10 times
# # print("*" * 10)

# # 2 + 3

# # X = 1
# # y = 3
# # print("hello guys", X, y)

# STUDENT_COUNT = 1000
# STRING_NAMES = "python \n programming "

# print(STUDENT_COUNT * 10, STRING_NAMES * 10)
# COURSE = "python"
# print(len(COURSE))
# print(COURSE[0])
# print(COURSE[-1])
# print(COURSE[0:3])

# # escape sequences
# # \"
# first = "Lucie"
# last = "Niyomutoni"
# full = first + " " + last
# full2 = f"{last} {first}"
# print(full2)
# x = input("X: ")


# y = int(x) + 10

# # print(f"x: {x} , y:{y}")

# TEMPERATURE = 17
# if TEMPERATURE > 30:
#     print("it's warm")
#     print("Take a break")

# elif TEMPERATURE > 20:
#     print("it's normal")
# else:
#     print("it's cold here")
# print("DONE!!!")

# age = 12

# message = "elgible" if age >=18 else  "Not eligible"

# print(message)

# logical operators are and or not

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligble")
# else:
#     print("Not eligble")

# for number in range(4):
#     print(number, "Attempt", (number + 1) * ".")
# for number in range(10):
#     print((number + 1) * "*")
#     print(number)
# count = 0
# for i in range(1, 10):
#     if (i % 2 == 0):
#         count +=1
#         print(i)
# print(f"we have printed {count} even number")


# functions

# def greet(firt_name, last_name):
#     print(f"Hello  {firt_name} {last_name} there")
#     print("welcome abroad")


# greet("Lucie", "Niyomutoni")
# def get_greeting(name):
#     return f"hi {name}"


# message = get_greeting("Lucie")
# print(message)

# def increment(number,by):
#     return number + by

# fizz_buzz


# def fizz_buzz(number):
#     if  number % 3 == 0 and number % 5 == 0:
#         print("FUZZBUZZ")
  
#     elif number % 5 == 0:
#         print("BUZZ")
#     elif   number % 3 == 0:
#         print("FIZZ")
#     else:
#         print(number)


# fizz_buzz(5)
from ecommerce.shopping import sales

# print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__cached__)
print(sales.__file__)