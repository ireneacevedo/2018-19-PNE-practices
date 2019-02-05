class Seq:
    #a class for representing sequences
    def __init__(self, strbases):
        print('New sequence created!')

        self.strbases = strbases
    def len(self):
        return len(self.strbases)

class Gene(Seq):
    #this class is derived from the seq all the objects of class Gene will inheritage the methods from Seq Class
    pass

s1 = Gene('ACGTCCT')
s2 = Seq('AAGT')

l1 = s1.len()
l2 = s2.len()

str1 = s1.strbases
str2 = s2.strbases

print('Sequence 1: {}'.format(str1))
print('Length: {}'.format(l1))
print('Sequence 2 : {}'.format(str2))
print('Length: {}'.format(l2))
print('the end')