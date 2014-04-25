# code file for ex42
# Is-A, Has-A object & classes

## Animal is-a object  (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
## Is-a
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Is-a
class Cat(Animal):
    def __init__(self,name):
        ## ??
        self.name = name
       
## Has-a
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has a pet 
        self.pet = None
     
## Is-a     
class Employee(Person):
    def __init__(self, name,salary):
        ## 
        super(Employee,self).__init__(name)
        ## 
        self.salary = salary
    
## Has-a
class Fish(object):
    pass
    
## Is-a
class Salmon(Fish):
    pass

## Has-a  
class Halibut(object):
    pass

## rover is a dog
rover = Dog("Rover")

satan = Cat("Satan")

marry = Person("Marry")

marry.pet = satan

frank = Employee("Frank",120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut
