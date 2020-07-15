import unittest
from collections import Counter


def isPermutation(a, b):
    return Counter(a) == Counter(b)


class Test(unittest.TestCase):
    dataT = [("aaaa", "aaaa"), ("hello", "olelh"), ("", "")]
    dataF = [("abcds", "safsdf"), ("hello finn", "hello finneas"), ("   ", "")]

    def test_isPermutation(self):
        # true check
        for a, b in self.dataT:
            actual = isPermutation(a, b)
            self.assertTrue(actual)
        # false check
        for a, b in self.dataF:
            actual = isPermutation(a, b)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
