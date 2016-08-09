# Exercies 20
print "Exercise 20: Functions and Files\n"

#import module needed from associated package
from sys import argv

#identify arguments needed for the command line
script, input_file = argv

# Function to read and print all the contents of argument f, if something were
# specified within the read(), those params would dictate what to read
# Reading large files can do bad things so be specific (example is small file)
def print_all(f):
    print f.read()

# f.seek(offset, from_what) changes the file object's position. The position is
# computed from adding offset to a reference point; the reference point is
# selected by the from_what argument. A from_what value of 0 measures from
# the beginning of the file, 1 uses the current file position, and 2 uses
# the end of the file as the reference point. from_what can be omitted and
# defaults to 0, using the beginning of the file as the reference point.

# See MethodsOfFileObjects.py for more details

def rewind(f):
    f.seek(0)

# Print the value of line_count and then read one line of file object f
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open the file and assign it to a variable name so we can take actions on it
current_file = open(input_file)

# Print the function print_all using the argument current_file as defined above
print "First let's print the whole file:\n"
print_all(current_file)

#Print the function rewind using the argument current_file as defined above
print "Now let's rewind, kind of like a tape."
rewind(current_file)

# Note:
# The statement x = x + y which is essentially concatenation, adding y to
# whatever x is
# The statement x += y is equivalent to x = operator.iadd(x, y).
# Another way to put it is to say that z = operator.iadd(x, y) is equivalent
# to the compound statement z = x; z += y.
# a = iconcat(a, b) is equivalent to a += b for a and b sequences.

#Since we set seek(0) we are starting at the beginning of the document

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print "Let's print three lines using one line of code:"

current_line = 1
print_a_line(current_line, current_file) 

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex20.py test.txt
        # Exercise 20: Functions and Files
        #
        # First let's print the whole file:
        #
        # This is a test to see
        # if this text can be copied to a new file.
        # Let's see if it works.
        #
        # Hurray!!
        # The End.
        #
        # Now let's rewind, kind of like a tape.
        # Let's print three lines:
        # 1 This is a test to see
        #
        # 2 if this text can be copied to a new file.
        #
        # 3 Let's see if it works.


    # q: What is f in the print_all and other functions?
    # The f is a variable just like you had in other functions in Exercise 18,
    # except this time it's a file. A file in Python is kind of like an old
    # tape drive on a mainframe, or maybe a DVD player. It has a "read head,"
    # and you can "seek" this read head around the file to positions, then
    # work with it there. Each time you do f.seek(0) you're moving to the
    # start of the file. Each time you do f.readline() you're reading a line
    # from the file, and moving the read head to right after the \n that ends
    # that line. This will be explained more as you go on.

    # q:  Why does seek(0) not set the current_line to 0?
    # First, the seek() function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte (first byte) in the file. Second, current_line is just a variable and has no real connection to the file at all. We are manually incrementing it.

    # q: What is +=?
    # You know how in English I can rewrite "it is" as "it's"? Or I can rewrite "you are" as "you're"? In English this is called a contraction, and this is kind of like a contraction for the two operations = and +. That means x = x + y is the same as x += y.

    # q: How does readline() know where each line is?
    # Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far. The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.

    # q: Why are there empty lines between the lines in the file?
    # The readline() function returns the \n that's in the file at the end of that line. Add a , at the end of your print function calls to avoid adding double \n to every line.
