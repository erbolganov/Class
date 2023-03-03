# class User:
#     def showInfo(selfself, name):
#         print(f"Name is {name}")
# vasya = User()
# vasya.showInfo("Vasya")
##-----------------------------------------------------------------
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def showInfo(self):
#         print(f"Name is {self.name}, Age is {self.age}")
# vasya = User("Vasya", 25)
# vasya.showInfo()
# #--------------------------------------------------------------------
# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else: print("Wrong age!!!")
#
#     @property
#     def name(self):
#         return self.__name
#     def display_info(self):
#         print(f"Name is {self.__name}, Age is {self.__age}")
#
# tom = Person("Tom")
# tom.display_info()
# tom.age = -995
# print(tom.age)
# tom.age = 36
# tom.display_info()
# #------------------------------------------------------------------------------

# class Home:
#     def __init__(self, amount, square):
#         self.amount = amount
#         self.square = square
#
#     def square_Person(self):
#         print(f"Square for per Person: {int(square)/int(amount)}")
#
#
# square = input("How square (kv.m) your home?  ")
# amount = input("How many people live?  ")
# c = Home(amount, square)
# c.square_Person()

# ----------------------------------------------------------------------------------------
class Car:
    def __init__(self, key, petrol):
        self.__key = key
        self.__petrol = petrol

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if self.key == "+":
            print("Push gas!")
        else: print("Key is not on!!!")

    @property
    def petrol(self):
        return self.__petrol

    @petrol.setter
    def petrol(self, petrol):
        if 5 < self.petrol < 40:
            print("You can go:)")
        else: print("Petrol is not enough!")
key = input("Please on (+) the key: ")
petrol = int(input("Enter amount of petrol: "))
go = Car(key, petrol)
go.key = key
go.petrol = petrol

