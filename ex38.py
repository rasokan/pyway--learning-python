# code file for ex38
# Doing things to Lists

# What is it talking about?
    
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not ten things in that list, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Days", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d item now" % len(stuff)
    
print "There we go: ", stuff
print "Let's do something with stuff."

print stuff[1]
print stuff[-1] #whoa fancy
print stuff.pop()
print ' '.join(stuff) # ' '.join(things) is join(' ', things).
print '#'.join(stuff[3:5]) # That's getting a "slice" from the stuff list that is from element 3 to element 4, meaning it does not include element 5. 
# It's similar to how range(3,5) would work.
 
