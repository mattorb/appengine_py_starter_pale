import random
import unittest
import baseunittest

class TestSequenceFunctions(baseunittest.GaeBaseUnitTest):
    def setUp(self):
        super(TestFetchAndParse, self).setUp()

    def tearDown(self):
        super(TestFetchAndParse, self).tearDown()

    def testshuffle(self):
        seq = range(10)
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(seq)
        seq.sort()
        self.assertEquals(seq, range(10))

if __name__ == '__main__':
    unittest.main()