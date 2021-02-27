from itertools import permutations, combinations_with_replacement
from Bio.Seq import Seq


def generator(n):
    nucl = 'ACTG'
    result = []
    perm_comb = set()
    for i in range(1, n + 1):
        for elem in permutations(nucl, i):
            perm_comb.add(''.join(elem))
        for elem in combinations_with_replacement(nucl, i):
            perm_comb.add(''.join(elem))
        result.extend(list(filter(lambda x: x not in result, perm_comb)))
    return result


# codon_type specifies the table of codons, codon_type=1 refers to Standard table
def dna_to_protein(path, codon_type=1):
    with open(path) as f, open('file_out.fasta', 'w+') as w:
        my_iterator = iter(f)
        while True:
            try:
                flag = next(my_iterator)
            except StopIteration:
                break
            if flag.startswith('>'):
                w.write(flag)
            else:
                gene = Seq(flag.strip())
                w.write(str(gene.translate(table=codon_type)) + '\n')


