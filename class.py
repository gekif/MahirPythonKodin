# class Person:
#     nama = "Cebi"

# obj =  Person()
# print(type(obj))
# print(obj.nama)


# Contoh angka

class Angka:
    jumlah = 5


a = Angka()
# print(a.jumlah)

b = Angka()
# print(b.jumlah)


#  Init Function

'''
class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def greet(self):
        print("Halo,", self.name + "!")

p1 =  Person("Cebi", 30, 50)
p2 =  Person("Bapu", 50, 25)

# print(p1.name)
# print(p1.age)
# print(p1.score)

# print(p1.__dict__)
# print(p2.__dict__)

p1.greet()
p2.greet()
'''


class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello")


class Cat(Animals):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight


class Dog(Animals):
    def __init__(self, name, age, types):
        super().__init__(name, age)
        self.type = types


puddle = Dog("Puddle", 20, "Cuwawa")
print(puddle)
