
# Exercise 14

# Sys - access to variables used or maintained by the interpreter
# and functions that interact strongly with the interpreter.

# https://docs.python.org/2/library/sys.html

# Another example of importing module from a package
# from collections import counter

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)


# MacBook-Pro-6:HelloWorld jessicadeluca$ python ex14.py Jessica
# Hi Jessica, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me Jessica?
# > Yes
# Where do you live Jessica?
# > San Francisco
# What kind of computer do you have?
# > Mac
#
# Alright, so you said 'Yes' about liking me.
# You live in 'San Francisco'.  Not sure where that is.
# And you have a 'Mac' computer.  Nice.
