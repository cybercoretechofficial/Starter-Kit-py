import unittest
from myproject.module1 import greet
from myproject.utils.helpers import add_numbers

class TestMyProject(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Tester"), "Hello, Tester! This is Module 1 working fine.")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
