# code file for ex17
# More files 

# import 'argv' as a variable
from sys import argv
# import 'exists' as a function 
from os.path import exists

# imply how this works in the shell code 
script, from_file, to_file = argv

print "Coping from %s to %s." % (from_file, to_file )

# we could do these two lines on one line, how ?
# only need to use a ';' to connect 
#in_file = open(from_file);indata = in_file.read()

# new version 
indata = open(from_file).read()


print "The input file is %d bytes long. " % len(indata )

print "Does the output file exist %r ?" % exists(to_file )
print "Ready, hit RETURN to cotinue, CTRL-C to abort." 
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()





