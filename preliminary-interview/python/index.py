### Python OOP

class Animal:
    def make_sound(self,val):
        return f"{val}"


class Dog(Animal):
    def make_sound(self, val):
        return super().make_sound(val) +" dog specific sound"
    
    
    
dog = Dog()
print(dog.make_sound('Woo'))

######### Encapsulation

# Encapsulation is the concept of bundling data (attributes) 
# and methods (functions) that operate on the data within one class, 
# and restricting direct access to some of the object's components.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    
######### Polymorphism

# Polymorphism allows objects of different classes to be treated 
# as objects of a common superclass, usually by overriding methods.

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  # Woof
make_animal_speak(Cat())  # Meow


############# abstraction

########################## abstractions 
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print('woof')


class Dog(Animal):
    def test(self,data):
        return 'ddd'

    def make_sound(self):
        return super().make_sound()
    

class Cat(Animal):
    def test(self,data):
        return 'howw'
    def make_sound(self):
        return super().make_sound()

d = Cat().make_sound()
print(d)




########### Dictionary sort,and more