from Seq import Seq

#main programm

sequence_1 = Seq('ACGTTACGGTACGT')
sequence_2 = Seq('TGCAAGTACGATTA')
sequence_3 = Seq.complement(sequence_1)
sequence_4 = Seq.reverse(sequence_3)

ls = [sequence_1, sequence_2, sequence_3, sequence_4]
number = 1

for sequence in ls:
    print('\n')
    print('Sequence {} : {}'.format(number, sequence.strbases))
    print(' Length: {}'.format(len(sequence.strbases)))
    print(' Bases count: A:{}, C :{}, G:{}, T:{} '.format(sequence.count('A'), sequence.count('C'),
        sequence.count('G'), sequence.count('T')))
    print(' Bases percentage: A:{}, C:{}, G:{}, T:{} '.format(sequence.perc('A'), sequence.perc('C'),
        sequence.perc('G'), sequence.perc('T')))
    number += 1




