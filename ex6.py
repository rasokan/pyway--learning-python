# code file for ex6
# Strings and Text

x = "There are %d types of people."  % 10
binary = "binary"
do_not = "don't"
# str in str 1st
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print(y)
# str in str 2nd
print ("I said : %r." % x )
# str in str 3rd 
print ("I also said :%r." % y)

hilarious = False
# str in str 4th 
joke_evaluation = "Isn't that joke so funny?! %r"

print ("Isn't that joke so funny?! %r" % hilarious) 
# equal to 
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

# exlain ? 
# ANS: maybe here the + is like a strlen function in 'C' 
print( w + e)
