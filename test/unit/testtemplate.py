import random
import unittest
import baseunittest

class TestExample(baseunittest.GaeBaseUnitTest):
    def setUp(self):
        super(TestExample, self).setUp()

    def tearDown(self):
        super(TestExample, self).tearDown()

    def testshuffle(self):
        seq = range(10)
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(seq)
        seq.sort()
        self.assertEquals(seq, range(10))

if __name__ == '__main__':
    unittest.main()