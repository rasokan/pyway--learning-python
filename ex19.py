# code for ex 19
# Functions, Variables 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %r cheese." % cheese_count
	print "You have %r boxes of crackers." % boxes_of_crackers
	print "Now that's enough for a party."
	print "Print a blanket.\n"

print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use scripts from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers = (amount_of_cheese, amount_of_crackers)

# error?
print "We can even do math inside:"
cheese_and_crackers(20+10, 40-10)

# error?
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 1000, amount_of_crackers + 20000)


#We can even do math inside:
#	Traceback (most recent call last):
#		  File "ex19.py", line 20, in <module>
#		      cheese_and_crackers(20+10, 40-10)
#			  TypeError: 'tuple' object is not callable''""

