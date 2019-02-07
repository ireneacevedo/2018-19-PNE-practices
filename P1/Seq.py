class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp = ''
        for letter in self.strbases:
            self.strbases = self.strbases.upper()
            if letter == 'A':
                comp += 'T'
            elif letter == 'C':
                comp += 'G'
            elif letter == 'G':
                comp += 'C'
            elif letter == 'T':
                comp += 'A'
        return comp

    def reverse(self):
        seq_rev = self.strbases[::-1]
        return seq_rev

    def count(self, base):
        self.base = base
        number_base = self.strbases.count(base)
        return number_base

    def perc(self, base):
        self.base = base
        percentage = round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
        return percentage






