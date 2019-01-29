
chain = str(input('Enter a sequence:'))
chain = chain.upper()
countA = 0
countC = 0
countT = 0
countG = 0
length = len(chain)
for letter in chain:
    if letter == 'A':
        countA += 1
    if letter == 'C':
        countC += 1
    if letter == 'T':
        countT += 1
    if letter == 'G':
        countG += 1

if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
    print('The sequence has no A,C,G or T')

print('Total length:{}'.format(length))
print('A:{}'.format(countA))
print('C:{}'.format(countC))
print('T:{}'.format(countT))
print('G:{}'.format(countG))
