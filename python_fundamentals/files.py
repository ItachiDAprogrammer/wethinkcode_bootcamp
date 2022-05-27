# The input function
"""
When the function executes, program flow will be stopped until the user has given input
This is a synchronous function
@returns a String
"""
name = input("What is your name?")

# The print function
print("I display information")

# The open function 
"""
This is a key function when working with files in Python
@params filename, mode
I support the following modes:
- "r" - read: Opens a file for reading, error if file does not exist
- "a" - append: Opens a file for appending, creates file if it does not exist
- "w" - write: Opens a file for writing, creates the file if it does not exist
- "x" - create: Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode:
- "t" - text: Default value. Text mode
- "b" - binary: Binary mode (e.g. images) Syntax
"""
f = open("demofile.txt")

# Read a file 
""" 
The open() function returns a file object, which has a read() method for reading the content of the file:
"""
f = open("demofile.txt")
print(f.read())

""" 
You can return one line by using the readline() method:
"""
print(f.readline())
print(f.readline())
""" 
By calling readline() two times, you can read the two first lines:
"""

# Closing a file 
""" 
It is a good practice to always close the file when you are done with it.
@note - You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file
"""
f.close()

# Write a file 
""" 
To write to an existing file, you must add a parameter to the open() function:

a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

# Open the file and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

""" 
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""

# Delete a file
""" 
To delete a file, you must import the OS module, and run its os.remove() function:
@params filename
"""
from genericpath import exists
import os
os.remove("demofile.txt")

""" 
To avoid getting an error, you might want to check if the file exists before you try to delete it: 
@note To delete an entire folder, use the os.rmdir() method
"""
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
