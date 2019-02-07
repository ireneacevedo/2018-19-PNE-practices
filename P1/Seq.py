class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        string = ''
        for letter in self.strbases:
            self.strbases = self.strbases.upper()
            if letter == 'A':
                string += 'T'
            elif letter == 'C':
                string += 'G'
            elif letter == 'G':
                string += 'C'
            elif letter == 'T':
                string += 'A'
        comp = Seq(string)
        return comp

    def reverse(self):
        seq_rev_str = self.strbases[::-1]
        seq_rev = Seq(seq_rev_str)
        return seq_rev

    def count(self, base):
        self.base = base
        number_base = self.strbases.count(base)
        return number_base

    def perc(self, base):
        self.base = base
        percentage = round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
        return percentage




