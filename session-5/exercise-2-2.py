from Bases import count_bases
#main program
seq1 = input('Please enter the first sequence: ')
seq2 = input('Please enter the second sequence: ') #ask for the sequences to the user
seq1 = seq1.upper()
seq2 = seq2.upper()
ls = [seq1, seq2]
count = 0

for i in ls:
    count += 1
    print('\n Sequence {}'.format(count),'\n')
    l = len(i)
    bases = count_bases(i) # we call the function
    print('The length of the sequence is: {}'.format(l), '\n')
    for keys in bases.keys():
        if l > 0:
            percentage = round(100.0*bases[keys] / l, 1)
            print('Base ',keys, '\n', 'Counter: {}'.format(bases[keys]))
            print(' Percentage: {}'.format(percentage), '%')
        else:
            percentage = 0