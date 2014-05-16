import unittest

from compiling._utils import *

class SourceGeneratorTestCase(unittest.TestCase):
    def test_source_generator_for_c(self):
        x = source_generator('c').next()
        self.assertTrue('target' in x)
        self.assertTrue('source' in x)

if __name__ == '__main__':
    unittest.main()
