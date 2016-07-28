# Exercise 18
print "Begin Exercise 18: Names, Variables, Code, Functions \n"

# Functions do three things:

    # They name pieces of code the way variables name strings and numbers.
    # They take arguments the way your scripts take argv.
    # Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

# You can create a function by using the word def in Python. I'm going to
# have you make four different functions that work like your scripts, and I'll
# then show you how each one is related.

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
# Unlike the argv example, our first line does not need to unpack the arguments
#
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
# Notice all functions have () followed by : in the defining line
# Functions have a name that describes what they do
# Functions have zero, one, or more arguments defined within ()
# Funcations are followed by and indented second line of code
# Unlike the argv example, our first line does not need to unpack the arguments
# Please read the FunctionsCheckList.txt file for steps when creating functions

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex18.py
        # Begin Exercise 18: Names, Variables, Code, Functions
        #
        # arg1: 'Zed', arg2: 'Shaw'
        # arg1: 'Zed', arg2: 'Shaw'
        # arg1: 'First!'
        # I got nothin'.

# Also see the KeyWordArgs.py doc for explanation of **kwargs (explained below)


# Functions can also be called using keyword arguments of the form kwarg=value.

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

    # accepts one required argument (voltage) and three optional arguments
    # (state, action, and type).

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

# In a function call, keyword arguments must follow positional arguments.
# All the keyword arguments passed must match one of the arguments accepted by
# the function (e.g. actor is not a valid argument for the parrot function),
# and their order is not important. This also includes non-optional arguments
# (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more
# than once. Here’s an example that fails due to this restriction:

>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: function() got multiple values for keyword argument 'a'


# When a final formal parameter of the form **name is present, it receives a
# dictionary (see Mapping Types — dict) containing all keyword arguments except
# for those corresponding to a formal parameter. This may be combined with a
# formal parameter of the form *name (described in the next subsection) which
# receives a tuple containing the positional arguments beyond the formal
# parameter list. (*name must occur before **name.) For example, if we define
# a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

# It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# and of course it would print:

        # -- Do you have any Limburger ?
        # -- I'm sorry, we're all out of Limburger
        # It's very runny, sir.
        # It's really very, VERY runny, sir.
----------------------------------------
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch

# Note that the list of keyword argument names is created by sorting the
# result of the keywords dictionary’s keys() method before printing its contents;
# if this is not done, the order in which the arguments are printed is undefined.
