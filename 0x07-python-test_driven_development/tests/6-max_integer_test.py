import unittest

max_integer = __import__('6-max_integer').max_integer


class TestmaxInt(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_random(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
        self.assertEqual(max_integer([5, 2, 3, 4, 1]), 5)
        self.assertEqual(max_integer([1.5, -0.6, -5, -6]), 1.5)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer("salah"), 's')
        self.assertEqual(max_integer(["abc", "def"]), "def")


if __name__ == '__main__':
    unittest.main()
