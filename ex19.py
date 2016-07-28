# Exercise 19
print "Exercise 19: Functions and Variables\n"

# The variables in your function are not connected to the variables in your
# script. Here's an exercise to get you thinking about this:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


        # MacBook-Pro-6:HelloWorld jessicadeluca$ python ex19.py
        # Exercise 19: Functions and Variables
        #
        # We can just give the function numbers directly:
        # You have 20 cheeses!
        # You have 30 boxes of crackers!
        # Man that's enough for a party!
        # Get a blanket.
        #
        # OR, we can use variables from our script:
        # You have 10 cheeses!
        # You have 50 boxes of crackers!
        # Man that's enough for a party!
        # Get a blanket.
        #
        # We can even do math inside too:
        # You have 30 cheeses!
        # You have 11 boxes of crackers!
        # Man that's enough for a party!
        # Get a blanket.
        #
        # And we can combine the two, variables and math:
        # You have 110 cheeses!
        # You have 1050 boxes of crackers!
        # Man that's enough for a party!
        # Get a blanket.

#q: What if I want to ask the user for the numbers of cheese and crackers?
# You need to use int() to convert what you get from raw_input().

#q: Does making the variable amount_of_cheese change the variable cheese_count
# in the function? No, those variables are separate and live outside the
# function. They are then passed to the function and temporary versions are made
# just for the function's run. When the function exits these temporary variables
# go away and everything keeps working. Keep going in the book and this should
# become clearer.

#q: can you call a function within a function ? Yes
#q: is there a limit to the numebr of arguments you can have in a function?
# It depends on the version of Python and the computer you're on, but it is
# fairly large. The practical limit though is about five arguments before the
# function becomes annoying to use.

#q: What if I want to ask the user for the numbers of cheese and crackers?
# You need to use int() to convert what you get from raw_input().
