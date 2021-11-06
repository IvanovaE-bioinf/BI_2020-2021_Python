# seq_type possible values: dna, rna
# possible nucleotides in seq: A, C, T, G, U, N, and in lowercase
# every out sequence in 5' to 3' orientation
# your sequence will be converted to uppercase

class NucleicAcid:
    seq_type = ''

    def __init__(self, sequence):
        self.seq = sequence.upper()

    def __universal_compliment(self, nucleotides):
        s = self.seq
        s = list(s)
        compliment = []
        for elem in s:
            compliment.append(nucleotides[elem])
        compliment.reverse()
        return ''.join(compliment)

    def reverse_compliment(self):
        if self.seq_type == 'dna':
            dna_to_dna = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
            return self.__universal_compliment(dna_to_dna)
        elif self.seq_type == 'rna':
            rna_to_rna = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
            return self.__universal_compliment(rna_to_rna)
        else:
            raise TypeError('Sequence type is not defined for this class.')

    def gc_count(self):
        s = self.seq
        seq_lst = list(s)
        seq_lst = [1 if i in ['C', 'G'] else 0 for i in seq_lst]
        return round((sum(seq_lst) / len(seq_lst)) * 100, 1)

    def __str__(self):
        return self.seq

    def __iter__(self):
        return iter(self.seq)

    def __hash__(self):
        return hash(self.seq + self.seq_type)

    def __eq__(self, other):
        a = self.seq
        b = other.seq.upper()
        if self.seq_type == other.seq_type and a == b:
            return True
        else:
            return False


class Rna(NucleicAcid):
    seq_type = 'rna'

    def __init__(self, sequence):
        super().__init__(sequence)


class Dna(NucleicAcid):
    seq_type = 'dna'

    def __init__(self, sequence):
        super().__init__(sequence)

    def transcribe(self):
        x = self.seq
        rna_object = Rna(x.replace('T', 'U'))
        return rna_object
