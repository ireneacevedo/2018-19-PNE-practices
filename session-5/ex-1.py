def count_a(seq):
    counter = 0
    for elem in seq:
        if elem == 'A':
            counter += 1
    return counter

#main program
s = input('Please enter the sequence: ')
number_a = count_a(s)
print('The number of As in the sequence is: {}'.format(number_a))

l = len(s)


print('The lenght of the seq is:{}'.format(l))

#the percentage of As in the sequence
if l > 0:
    perc= round(100.0*number_a/l, 1)
else:
    perc = 0
print('The percentage of AS in the seq is:{}'.format(perc),'%')
