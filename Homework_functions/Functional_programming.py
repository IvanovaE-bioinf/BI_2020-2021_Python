import itertools
from Bio.Seq import Seq


def generator(n):
    for i in range(1, n + 1):
        for element in itertools.product('ACGT', repeat=i):
            yield ''.join(list(element))


def dna_to_protein(path_to_fasta, codon_type='Standard'):
    with open(path_to_fasta) as f:
        header = f.readline()
        dna_seq = ''
        for line in f:
            if not line.startswith('>'):
                dna_seq += line.rstrip()
            else:
                dna_seq = Seq(dna_seq)
                protein = str(dna_seq.translate(table=codon_type))
                protein_seq = header + protein
                header = line
                dna_seq = ''
                yield protein_seq
        dna_seq = Seq(dna_seq)
        protein = str(dna_seq.translate(table=codon_type))
        protein_seq = header + protein
        yield protein_seq
