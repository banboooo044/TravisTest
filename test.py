#-*- coding:utf-8 -*-
import unittest
from script import myabs

class MyAbsTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1, myabs(1))
        self.assertEqual(1, myabs(-1))
        self.assertEqual(0, myabs(0))

if __name__ == '__main__':
    unittest.main()
