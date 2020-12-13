# Task 1
# Inheritance is when one class can copy all the properties and methods
# of another class and add its own new methods and properties.
class Person:
    def __init__(self, name="Ramazan", age="17"):
        self.name = name
        self.age = age
    def showName(self):
        return self.name
    def showAge(self):
        return self.age

class Sportsmen(Person):
    def __init__(self, sport_type="Football", experience="2 years"):
        Person.__init__(self)
        self.sport_type = sport_type
        self.experience = experience
    def showInformation(self):
        answer = "Name: " + self.name + "\n"
        answer += "Age: " + self.age + "\n"
        answer += "Sport type: " + self.sport_type + "\n"
        answer += "Experience: " + self.experience
        return answer

ramazan = Sportsmen()
print(ramazan.showInformation())
# Result:
# Name: Ramazan       
# Age: 17
# Sport type: Football
# Experience: 2 years

# Task 2
class Animal:
    def __init__(self, age):
        self.hungry_level = 50
        self.age = age
    def isHungry(self):
        if self.hungry_level > 30:
            return "I'm hungry"
        else:
            return "I'm not hungry"
    def showAge(self):
        return self.age
    def feed(self, meal):
        self.hungry_level -= meal
        if self.hungry_level < 0:
            self.hungry_level = 0

class Pet(Animal):
    def __init__(self, name, pet_type):
        Animal.__init__(self, 3)
        self.name = name
        self.type = pet_type
    def saySomething(self):
        if self.type == "Cat":
            return "Meow"
        elif self.type == "Dog":
            return "Bark"
        else:
            return "Aaaaa"

myPet = Pet("Barsik", "Cat")
print(myPet.isHungry())
myPet.feed(40)
print(myPet.isHungry())
print(myPet.showAge())
print(myPet.saySomething())
# Result:
# I'm hungry
# I'm not hungry
# 3
# Meow

Task 3
Multilevel inheritance is when one class inherits from another and the third class inherits from the first. For example, this is how I inherit from my father, and my father inherits from my grandfather. The inheritance hierarchy is when several classes are inherited from one class. For example, if a father has several sons, then they all inherit from him.