# Exercise 17
# Important functions
    # open(),read(),raw_input(),len(),exists(), write(), close()
print "Begin Exercise 17: More Files \n"


#Copy one file to another file

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex17.py test.txt test_copy2.txt
        # Begin Exercise 17: More Files
        #
        # Copying from test.txt to test_copy2.txt
        # The input file is 106 bytes long
        # Does the output file exist? False
        # Ready, hit RETURN to continue, CTRL-C to abort.


# Steps for interesting clean output
    # State what the job does
    # State the file size
    # State is the output file exists or not using exists()
    # Ask for explicit consent before running the job
    # Return statement once job is successfully finished
