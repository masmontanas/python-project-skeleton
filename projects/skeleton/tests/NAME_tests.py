import unittest
from nose import *
import NAME

class TestCase(unittest.TestCase):
    def setup(self):
        print("SETUP!")

    def teardown(self):
        print("TEAR DOWN!")

    def test_basic(self):
        assert 1 == 1
        print("I RAN!")

if __name__ == '__main__':
    unittest.main()