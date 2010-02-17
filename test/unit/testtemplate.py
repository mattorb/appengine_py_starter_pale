import random
import unittest
import baseunittest

class TestSequenceFunctions(baseunittest.GaeBaseUnitTest):

    def setUp(self):
        self.seq = range(10)

    def testshuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEquals(self.seq, range(10))

if __name__ == '__main__':
    unittest.main()