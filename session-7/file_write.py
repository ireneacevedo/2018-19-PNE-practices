NAME = 'mynotes.txt'

# Open the file
myfile = open(NAME,'r')
#myfile is an object

print('File opened:{}'.format(myfile.name))

contents = myfile.read()

print('The file contents are: {}'.format(contents))

myfile.close()

f = open(NAME, 'a')
f.write('THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE')
f.close()
print('The end')