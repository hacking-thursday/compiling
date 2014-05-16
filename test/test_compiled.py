#!/usr/bin/env python
import unittest

from compiling import compiled


class CompiledTestCase(unittest.TestCase):

    def test_compiled_for_c(self):
        self.assertEqual(compiled('.c'), '.o')
        self.assertEqual(compiled('test.c'), 'test.o')
        self.assertEqual(compiled('testc'), 'testc')
        self.assertEqual(compiled('test.cpp'), 'test.o')

if __name__ == '__main__':
    unittest.main()
