# note file for ex40+
# Modules, CLasses and Objects (IMPORTANT)

## MODULEs
import mystuff
mystuff.apple()
print mystuff.tangerine
#/* mystuff['apple']    // get apple from dicts
# * mystuff.apple()     // get apple func from the module
# * mystuff.tangerine   // get variable from the module  */


## CLASSES
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLE" 

## OBJECTS
thing = MyStuff() // instantiate
thing.apple()
print thing.tangeine


# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style 
thing = MyStuff()
thing.apple()
print thing.tangeine


