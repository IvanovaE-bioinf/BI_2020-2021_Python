import unittest
from classes import NucleicAcid, Rna, Dna


class TestDnaRna(unittest.TestCase):
    def setUp(self):
        self.dna = Dna('actgn')  # dna
        self.rna = Rna('acugn')  # rna
        self.acid = NucleicAcid('actg')  # some acid

    def test_reverse_compliment(self):
        self.assertEqual((self.dna.reverse_compliment(),
                          self.rna.reverse_compliment()), ('NCAGT', 'NCAGU'))
        with self.assertRaises(TypeError):
            self.acid.reverse_compliment()

    def test_gc_count(self):
        self.assertEqual((self.dna.gc_count(), self.rna.gc_count(),
                          self.acid.gc_count()), (40, 40, 50))

    def test_transcribe(self):
        new_rna = self.dna.transcribe()
        self.assertEqual(new_rna, self.rna)


if __name__ == "__main__":
    unittest.main()
