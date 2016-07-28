# Learn Python The Hard Way
# http://learnpythonthehardway.org/book/

# iTerm for terminal
# iPython
# Atom as IDE (integrated developent environment) / Text Editor
# GitHub


# Exercise 1
print "Begin Exercise 1" + "\n"
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.' + "\n"

    # Hello World!
    # Hello Again
    # I like typing this.
    # This is fun.
    # Yay! Printing.
    # I'd much rather you 'not'.
    # I "said" do not touch this.

# Exercise 3
print "Begin Exercise 3"+"\n"
print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print 25 * 3 % 4
print 25 * 3
print 75 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2, "\n"

    # I will now count my chickens:
    # Hens 30
    # Roosters 97
    # 3
    # 75
    # 3
    # Now I will count the eggs:
    # 7
    # Is it true that 3 + 2 < 5 - 7?
    # False
    # What is 3 + 2? 5
    # What is 5 - 7? -2
    # Oh, that's why it's False.
    # How about some more.
    # Is it greater? True
    # Is it greater or equal? True
    # Is it less or equal? False


# Exercise 4
print "Begin Exercise 4" + "\n"
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

    # There are 100 cars available.
    # There are only 30 drivers available.
    # There will be 70 empty cars today.
    # We can transport 120.0 people today.
    # We have 90 to carpool today.
    # We need to put about 3 in each car.

print "Hey %s there." % "you" + "\n"
    # Hey you there.

    # What do you mean by "read the file backward"?
        # Very simple. Imagine you have a file with 16 lines of code in it. Start at line 16,
        # and compare it to my file at line 16. Then do it again for 15,
        # and so on until you've read the whole file backward.

# Exercise 5
print "Begin Exercise 5" + "\n"

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "%s is really fat. He weighs %d pounds." % (my_name, my_weight)

    # Let's talk about Zed A. Shaw.
    # He's 74 inches tall.
    # He's 180 pounds heavy.
    # Actually that's not too heavy.
    # He's got Blue eyes and Brown hair.
    # His teeth are usually White depending on the coffee.
    # Zed A. Shaw is really fat. He weighs 180 pounds.
    # If I add 35, 74, and 180 I get 289.

# Format specifiers:  %s for string, %d for decimal, %r for debugging
# What are formatters?
# They tell Python to take the variable on the right and put it in to replace the %s with its value.
# I don't get it, what is a "formatter"? Huh? The problem with teaching you programming is that
# to understand many of my descriptions you need to know how to do programming already.
# The way I solve this is I make you do something, and then I explain it later.
# When you run into these kinds of questions, write them down and see if I explain it later.

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight) + "\n"

# Begin Exercise 6


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

    # There are 10 types of people.
    # Those who know binary and those who don't.

print "I said: %r." % x
    # I said: 'There are 10 types of people.'.

# Notice the stylistic choice of using single quotes and then the double quotes
# for a string with a string noted below
print "I also said: '%s'." % y
    # I also said: 'Those who know binary and those who don't.'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
    # Isn't that joke so funny?! False

w = "This is the left side of..."
e = "a string with a right side."

    # This is the left side of...a string with a right side.

print w + e + "\n"

# What is the difference between %r and %s?
# Use the %r for debugging, since it displays the "raw" data of the variable,
# but the others are used for displaying to users.

# What's the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are for actually displaying variables to users.


# Begin Exercise 7
print "Begin Exercise 7" "\n"
# print a string
print "Mary had a little lamb."

# print a string with a format specifer for string 'snow'
print "Its fleece was white as %s." % 'snow'

# print a string with a format specifer for string 'black'
print "What about the %s sheep?" % 'black'
# Mistake: I forgot to have black in quotes, threw an error

print "And everywhere that Mary went."
print "." * 10  # what'd that do?
print "F$#@" * 4, "it"
# Mistake: Without the comma it returns the whole line as a string, need comma not () to isolate

#Create a string with format specifiers for multiple string and decimal values as well as a variable
selling = "What if we sold"
print "%s the %s sheep for $%d and the %s sheep for $%d?" % (selling, 'black', 10, 'white', 5)

    # Mary had a little lamb.
    # Its fleece was white as snow.
    # What about the black sheep?
    # ..........
    # F$#@F$#@F$#@F$#@ it
    # What if we sold the black sheep for $10 and the white sheep for $5?


paradise = "Paradise"
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
print "in %s" % paradise +"\n"
# Without the comma after end6 a new line is automatically created,
# The comma acts as a space between both print lines when it returns values
# It's bad form to go over 80 characters per line (ie- this line to the right ->)

# Exercise 8
print "Exercise 8" "\n"
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.") +"\n"
# Mistake: I forgot the commas for the last 4 sentences
# Mistake: The last 4 sentences >80 characters so I had to put on new lines
# Note: Used double quotes in lieu of single quoates due to conjunction: didn't
# Note: Only string values need quotes

    # 1 2 3 4
    # 'one' 'two' 'three' 'four'
    # True False False True
    # '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
    # 'I had this thing.' 'That you could type up right.'
    # "But it didn't sing." 'So I said goodnight.'

# Exercise 9
print "Exercies 9" +"\n"

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Note: "\n" adds a new line

print "Here are the days:", days
print "Here are the months:", months

print "Test"
print """There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6."""
print "Test"
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#Below code will only print the top line (ie - limiation of "" single line)
print "There's something going on here.",
"With the three double-quotes.",
"We'll be able to type as much as we like.",
"Even 4 lines if we want, or 5, or 6."


# Triple quotes on their own lines at beginning and end will add new lines

# Note: You can use ' or " or """ to wrap around strings
# They can use ' or " quotation marks (eg 'foo' "bar").
# The main limitation with these is that they don't wrap across multiple lines.
# That's what multiline-strings are for: These are strings surrounded by
# triple single or double quotes (''' or """) and are terminated only when
# a matching unescaped terminator is found. They can go on for as many
# lines as needed, and include all intervening whitespace.


    # Here are the days: Mon Tue Wed Thu Fri Sat Sun
    # Here are the months: Jan
    # Feb
    # Mar
    # Apr
    # May
    # Jun
    # Jul
    # Aug
    #
    # There's something going on here.
    # With the three double-quotes.
    # We'll be able to type as much as we like.
    # Even 4 lines if we want, or 5, or 6.


# Exercise 10
print "Exercise 10" +"\n"

# Sometimes you need to escape the ' or " within a string (use /)
print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string


# Tab a line in
tabby_cat = "\tI'm tabbed in."

# Add a new line mid string
persian_cat = "I'm split\non a line."

# Add a single backslash within a string 2 methods
backslash_cat = "I'm \\ a \\ cat."
backslash_cat2 = "I'm \ a \ cat."

# Make a formatted list 2 methods
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip
\t* Grass
"""
# Note: New line automatically created in output when formatted such here

print tabby_cat
print persian_cat
print backslash_cat
print backslash_cat2
print fat_cat
print fat_cat2


# Escape sequence list reference (notice the '\' preface)
# http://learnpythonthehardway.org/book/ex10.html

# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

print 'A "smart" man named %s with an IQ of %d.' % ("Steven", 140)
print 'A /"smart/" man named %r with an IQ of %r.' % ("Steven", 140)

# Sometimes you need to escape the ' or " within a string (use /)
print "I am 6'2\" %s with long %s." % ("tall", "arms")
print "I am 6'2\" %r with long %r." % ("tall", "arms")
print 'I am %d\'%d" tall with %d" long %s.' % (6,2,36, "arms")
print 'I am %r\'%r" tall with %d" long %s.' % (6,2,36,"arms")
print "I am 6'2\""
# print "I am 6'2""
# The above throws and error without the escape sequence

print "\n" "End Of Exercise Block 1-10"+ "\n"
