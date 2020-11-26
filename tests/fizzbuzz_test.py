import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_fizzbuzz__15_returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))

    def test_fizzbuzz__4_returns_4_as_string(self):
        self.assertEqual("4", fizzbuzz(4))