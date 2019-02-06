def count_bases(seq):
    """"Counting number of bases in the sequence"""
    counter_a = 0
    counter_c = 0
    counter_g = 0
    counter_t = 0
    for elem in seq:
        if elem == 'A':
            counter_a += 1
        elif elem == 'C':
            counter_c += 1
        elif elem == 'G':
            counter_g += 1
        elif elem == 'T':
            counter_t += 1
    dict_bases = {'A': counter_a,'C': counter_c,'G': counter_g, 'T':counter_t}
    return dict_bases

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





