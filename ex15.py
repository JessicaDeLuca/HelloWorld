# Exercise 15
print "Exercise 15: Reading Files \n"


# What we want to do is "open" that file in our script and print it out.
# However, we do not want to just "hard code" the name ex15_sample.txt into
# our script. "Hard coding" means putting some bit of information that should
# come from the user as a string directly in our source code. That's bad because
# we want it to load other files later. The solution is to use argv or
# raw_input to ask the user what file to open instead of "hard coding"
# the file's name.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename

# Below txt.read() says "Hey txt! Do your read command with no parameters!
# Also note that the . gives the file a command in this case read()
print txt.read()
print txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()


    # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex15.py ex15_sample.txt
    # Exercise 15: Reading Files
    #
    # Here's your file 'ex15_sample.txt':
    # This is stuff I typed into a file.
    # It is really cool stuff.
    # Lots and lots of fun to have in here.
    #
    # Type the filename again:
    # > ex15_sample.txt
    # This is stuff I typed into a file.
    # It is really cool stuff.
    # Lots and lots of fun to have in here.

# Notes
# Lines 1-3 uses argv to get a filename. Next we have line 5 where we use a new command open. Right now, run pydoc open and read the instructions. Notice how like your own scripts and raw_input, it takes a parameter and returns a value you can set to your own variable. You just opened a file.

# Line 7 prints a little message, but on line 8 we have something very new
# and exciting. We call a function on txt named read. What you get back
# from open is a file, and it also has commands you can give it. You give a
# file a command by using the . (dot or period), the name of the command, and
# parameters. Just like with open and raw_input. The difference is that
# txt.read() says, "Hey txt! Do your read command with no parameters!"

# Steps:
# Call the file 2 methods (argv (better choice?) or raw_input)
# Open the file
# Read the file (or take defined action on it)

#q: Does txt = open(filename) return the contents of the file?
# No, it doesn't. It actually makes something called a "file object."
# You can think of a file like an old tape drive that you saw on mainframe
# computers in the 1950s, or even like a DVD player from today.
# You can move around inside them, and then "read" them, but the DVD player
# is not the DVD the same way the file object is not the file's contents.

#q: Why is there no error when we open the file twice?
# Python will not restrict you from opening a file more than once and
# sometimes this is necessary.

#q:  What does from sys import argv mean?
# For now just understand that sys is a package, and this phrase just says to
# get the argv feature from that package. You'll learn more about these later.
