from Bases import count_bases
#main program
seq = input('Please enter the sequence: ') #ask for the sequence to the user
seq = seq.upper()

bases = count_bases(seq) #we call the function
l = len(seq)


for keys in bases.keys():
    if l > 0:
        percentage = round(100.0*bases[keys] / l, 1)

        print('Base ',keys, '\n', 'Counter: {}'.format(bases[keys]))
        print(' Percentage: {}'.format(percentage), '%')
    else:
        percentage = 0
print('The length of the sequence is: {}'.format(l), '\n')