# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("D:\Python\Files\osama.txt")

# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("D:\Python\Files\osama.txt", "r")

print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read())
print(myFile.read(5))

print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

  print(line)

  if line.startswith("07"):

    break

# Close The File

myFile.close()


# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")

# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")



'''

    Python Files Handling
    Python Files With Keyword

'''