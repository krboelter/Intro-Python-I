"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os

cwd = os.getcwd()

with open(f'{cwd}/src/foo.txt') as f:
    read_data = f.read()

    print(read_data)    

    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
from pathlib import Path
new_file = Path(f'{cwd}/src/bar.txt')

if not new_file.is_file():

    with open(f'{cwd}/src/bar.txt', 'a+') as f:
        f.write('Hello World\n')
        f.write('abcdefg\n')
        f.write('1234567\n')
    
        f.close()

with open(f'{cwd}/src/bar.txt') as f:
    read_data = f.read()

    print(read_data)

    f.close()
