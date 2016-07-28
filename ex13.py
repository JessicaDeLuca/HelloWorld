
# Exercise 13
print "\n" "Begin Exercise 13: Parameters, Unpacking, Variables" "\n"

# In this exercise we will cover one more input method you can use to
# pass variables to a script (script being another name for your .py files).
# You know how you type python ex13.py to run the ex13.py file? Well the
# ex13.py part of the command is called an "argument." What we'll do now is
# write a script that also accepts arguments.



# On line 1 we have what's called an "import."
# Import modules or libraries from various packages

# Python module is just a python source file which can expose classes, functions
# and global variables
#
# Python package is simply a directory of Python modules (example is 'collections')
# Modules give you feature

# from collections import counter

# https://docs.python.org/2.7/library/collections.html
        # import mypackage.mymodule
        # or
        # from mypackage.mymodule import myclass
#
# The argv is the "argument variable," a very standard name in programming,
#that you will find used in many other languages. This variable holds the
#arguments you pass to your Python script when you run it. In the exercises
#you will get to play with this more and see what happens.
#
# Line 3 "unpacks" argv so that, rather than holding all the arguments,
# it gets assigned to four variables you can work with:
# script, first, second, and third. This may look strange, but "unpack" is
# probably the best word to describe what it does. It just says, "Take whatever
# is in argv, unpack it, and assign it to all of these variables on the
# left in order."


# In terminal type the below once in the correct directory 'HelloWorld':
# MacBook-Pro-6:HelloWorld jessicadeluca$ python ex13.py first 2nd 3rd
# Note the important part:
    # python ex13.py first 2nd 3rd

from sys import argv

script, first, second = argv

# script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
# print "Your third variable is:", third

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex13.py Barely Making It
        # The script is called: ex13.py
        # Your first variable is: Barely
        # Your second variable is: Making
        # Your third variable is: It

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex13.py Any Three Works
        # The script is called: ex13.py
        # Your first variable is: Any
        # Your second variable is: Three
        # Your third variable is: Works
        # MacBook-Pro-6:HelloWorld jessicadeluca$

# Note: You need to add the same number of values in the command line as
# that unpacked within the module code

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex13.py Any Two
        # The script is called: ex13.py
        # Your first variable is: Any
        # Your second variable is: Two

age = raw_input("How old are you? ")
Gender = "female"
print "%s! Omg you are old and %s, that's crazy!" % (age, Gender)

#q: Are the command line arguments strings?
# Yes, they come in as strings, even if you typed numbers on the command line.
# Use int() to convert them just like with int(raw_input()).

#q:What's the difference between argv and raw_input()?
# The difference has to do with where the user is required to give input.
# If they give your script inputs on the command line, then you use argv.
# If you want them to input using the keyboard while the script is running,
# then use raw_input().
