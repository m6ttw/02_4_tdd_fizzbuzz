import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("buzz", fizzbuzz(5))