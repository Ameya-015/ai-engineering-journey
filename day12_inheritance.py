class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

a = Animal("Generic")
c = Cat("Whiskers")

a.speak()
c.speak()


###########################################################################

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)  # Parent constructor call
        self.brand = brand

c = Car(4, "Toyota")
print(c.wheels)
print(c.brand)

###########################################################################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        print(f"{self.name} earns {self.salary}")

class Manager(Employee):    
    def __init__(self, name, salary, teamSize):
        super().__init__(name, salary)
        self.teamSize = teamSize

    def describe(self):
        print(f"{self.name} earns {self.salary} and manages a team of {self.teamSize}")

emp = Manager("Klaus", 50000, 5)
emp.describe()