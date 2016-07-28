
# Exercise 11

# Most of what software does is the following:

# Take some kind of input from a person.
# Change it.
# Print out something to show how it changed.

# raw_input

# name = raw_input("What is your name? ")
# print "Hello, %s." % name

print "Begin Exercise 11" + "\n"

print """
Why is this broken,
when I need to study,
for the rest of the afternon.
"""

#Terminal will ask the question and then require age input from user
print "How old are you?",
age = raw_input()

#Terminal will ask the question and then require age input from user
print "How tall are you?",
height = raw_input()

#Terminal will ask the question and then require age input from user
print "How much do you weigh?",
weight = raw_input()

# Given user input, the corresponding values with be returned
print "So, you're %r old, %r tall and %r heavy." % (
   age, height, weight)
# Mistake: %r returns raw feedback so escape sequence is not considered
# and '5\'6"'will be returned instead of just 5'6"


# Given user input, the corresponding values with be returned
print "So, you're %s old, %s tall and %s heavy." % (
   age, height, weight)

# q:I put my height in like this raw_input("6'2") but it doesn't work.
# You don't put your height in there, you type it directly into your Terminal.
# First thing is, go back and make the code exactly like mine.
# Next, run the script and when it pauses, type your height in at your keyboard.
# That's all there is to it.

# q: How do I get a number from someone so I can do math?
# That's a little advanced, but try x = int(raw_input())
# which gets the number as a string from raw_input() then converts it
# to an integer using int().

# q: What's the difference between input() and raw_input()?
# The input() function will try to convert things you enter as if they
# were Python code, but it has security problems so you should avoid it.

print "What is your name?",
Name = raw_input()
print "%s what city do you live in?" % Name,
City = raw_input()

print Name, "lives in", City

# Exercise 12

print "\n" "Begin Exercise 12" "\n"

# When you typed raw_input() you were typing the ( and ) characters,
# which are parenthesis characters. This is similar to when you used them
# to do a format with extra variables, as in "%s %s" % (x, y).
# For raw_input you can also put in a prompt to show to a person so he knows
# what to type. Put a string that you want for the prompt inside the () so
# that it looks like this:
# Example:  y = raw_input("Name? ")

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)

#Tip: In terminal type 'pydoc isinstance' or 'pydoc raw_input' for definition
# to get our of pydoc type 'q' to quit

# %r is for debugging and %s is for display
