# Example of reading a file located in our local file system

NAME = 'mynotes.txt'

# Open the file
myfile = open(NAME,'r')
#myfile is an object

print('File opened:{}'.format(myfile.name))

contents = myfile.read()

print('The file contents are: {}'.format(contents))