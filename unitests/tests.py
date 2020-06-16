import unittest
from code import add_two_ints


class TestMyCode(unittest.TestCase):
    def test_add_two_ints(self):
        self.assertEqual(add_two_ints(10, 20), 30)

    def test_add_two_incorrect_ints(self):
        self.assertNotEqual(add_two_ints(10, 20), 40)

    def test_add_two_ints_failure(self):
        self.assertRaises(add_two_ints(10, 'hello'), ValueError)