# Python Software Foundation
# https://docs.python.org/2.7/tutorial/inputoutput.html

7.2.1. Methods of File Objects
# The rest of the examples in this section will assume that a file object
# called f has already been created.

# To read a file’s contents, call f.read(size), which reads some quantity
# of data and returns it as a string. size is an optional numeric argument.
# When size is omitted or negative, the entire contents of the file will be
# read and returned; it’s your problem if the file is twice as large as your
# machine’s memory. Otherwise, at most size bytes are read and returned.
# If the end of the file has been reached, f.read() will return an empty
# string ("").

>>>
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
# f.readline() reads a single line from the file; a newline character (\n)
# is left at the end of the string, and is only omitted on the last line of
# the file if the file doesn’t end in a newline. This makes the return value
# unambiguous; if f.readline() returns an empty string, the end of the file
# has been reached, while a blank line is represented by '\n', a string
# containing only a single newline.

>>>
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
# For reading lines from a file, you can loop over the file object. This is
# memory efficient, fast, and leads to simple code:

>>>
>>> for line in f:
        print line,

This is the first line of the file.
Second line of the file

# If you want to read all the lines of a file in a list you can also use
# list(f) or f.readlines().

# f.write(string) writes the contents of string to the file, returning None.

>>>
>>> f.write('This is a test\n')

# To write something other than a string, it needs to be converted to a string
# first:

>>>
>>> value = ('the answer', 42)
>>> s = str(value)
>>> f.write(s)

# f.tell() returns an integer giving the file object’s current position in
# the file, measured in bytes from the beginning of the file. To change
# the file object’s position, use f.seek(offset, from_what). The position is
# computed from adding offset to a reference point; the reference point is
# selected by the from_what argument. A from_what value of 0 measures from
# the beginning of the file, 1 uses the current file position, and 2 uses
# the end of the file as the reference point. from_what can be omitted and
# defaults to 0, using the beginning of the file as the reference point.

>>>
>>> f = open('workfile', 'r+')
>>> f.write('0123456789abcdef')
>>> f.seek(5)      # Go to the 6th byte in the file
>>> f.read(1)
'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
>>> f.read(1)
'd'

# When you’re done with a file, call f.close() to close it and free up any
# system resources taken up by the open file. After calling f.close(), attempts
# to use the file object will automatically fail.

>>>
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: I/O operation on closed file

#It is good practice to use the with keyword when dealing with file objects.
# This has the advantage that the file is properly closed after its suite
# finishes, even if an exception is raised on the way. It is also much shorter
# than writing equivalent try-finally blocks:

>>>
>>> with open('workfile', 'r') as f:
...     read_data = f.read()
>>> f.closed
True

# File objects have some additional methods, such as isatty() and truncate()
# which are less frequently used; consult the Library Reference for a complete
# guide to file objects.
