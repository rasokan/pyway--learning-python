# code file for ex44
# Inheritance VS Composition P142

class Parent(object):
    def implicit(self):
        print "PARENT implicit"
        
    def override(self):
        print "PARENT override"
        
    def altered(self):
        print "PARENT altered()"    

class Child(Parent):
    def override(self):
        print "CHILD override"
        
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    


# Multiple Inheritance
class BadStuff(object):
    pass
    
class SuperFun(Child, BadStuff):
    pass

class Other(object):
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        
## child ver2
class Child(object):
    def __init__(self):
        self.other = Other()
        
    def implicit():
        self.other.implicit()
        
    def override():
        print "CHILD override()"
        
    def altered():
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
#####################################################
## using super() in class 
#####################################################
# class Child(Parent):
#     def __init__(self,stuff):
#         self.stuff = self
#         super(Child, self).__init__()
#
#####################################################






dad = Parent()
son = Child()

## implicit
dad.implicit()
son.implicit()

## override
dad.override()
son.override()

## altered
dad.altered()
son.altered()
