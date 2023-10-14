# def greet():
#     print("Hello Bro")

# greet()

# Passing Arguments
'''
def greet(name):
    print("Hello", name)

greet("Cebi")
greet("Teddy")
greet("Jenny")
'''

'''
def introduction(name, age):
    print(name, age)

introduction("Fikar", 20)
'''


# Lambda Function

def add5(x):
    return x + 5

# print(add5(2))

add5 = lambda x: x + 2
print(add5(2))