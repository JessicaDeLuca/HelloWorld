# Exercise 16

print "Exercise 16: Reading and Writing Files \n"

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Assign the file to a variable that can be acted upon
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Instead of repetitive writing above for each line, Use strings, formats,
# and escapes to print out line1, line2, and line3 with just one
# target.write() command instead of six.

#Mistake first attempt see error below for details
    # Traceback (most recent call last):
    # File "ex16.py", line 36, in <module>
    # target.write(line1,"\n",line2,"\n",line3,"\n")
    # > TypeError: function takes exactly 1 argument (6 given)

# Used format specifiers since the function takes exactly 1 argument
target.write("%s\n%s\n%s\n" % (line1,line2,line3))

print "And finally, we close it."
target.close()

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex16.py text_ex16.txt
        # Exercise 16: Reading and Writing Files

        # We're going to erase 'text_ex16.txt'.
        # If you don't want that, hit CTRL-C (^C).
        # If you do want that, hit RETURN.
        # ?
        # Opening the file...
        # Truncating the file.  Goodbye!
        # Now I'm going to ask you for three lines.
        # line 1: try this again
        # line 2: and again
        # line 3: and again!
        # I'm going to write these to the file.
        # And finally, we close it.

# Note: open() default mode is read or the r param. Other params need to be
# directly specified, hence the w param in the above code. Also the a param
# for append can be used.
