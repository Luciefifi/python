try:
    age = int(input("Age : "))
except ValueError :
    print("you did not enter a valid age")
else:
    print("no exceptions were thrown")
print("program continues")