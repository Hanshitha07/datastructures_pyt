# # def outer():
# #     x = "outer"

# #     def inner():
# #         nonlocal x
# #         x = "inner"
# #     inner()
# #     print(x)

# # outer()  # Output: inner

# x = "global"

# def outer():
#     x = "enclosing"

#     def inner():
#         global x
#         x = "local"
#         print(x)
#     inner()

# outer()
# print(x)  # Output: local

# class Car:
#     # attributes (data / variables)
#     brand = "Tesla"
#     color = "Red"
    
#     # method (function inside class)
#     def drive(self):
#         print("The car is moving!")
# # Creating objects (instances of Car)
# car1 = Car()
# car2 = Car()

# print(car1.brand)   # Tesla
# print(car2.color)   # Red

# car1.drive()        # The car is moving!
# car2.drive()        # The car is moving!

class Dog:
    # constructor
    def __init__(self, name, breed):
        self.name = name   # attribute
        self.breed = breed # attribute

# creating objects
dog1 = Dog("Bruno", "Labrador")
dog2 = Dog("Simba", "German Shepherd")

print(f"{dog1.name},- {dog1.breed}")
print(f"{dog2.name},- {dog2.breed}")
