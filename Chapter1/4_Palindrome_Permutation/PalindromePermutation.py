import unittest


def palindromePermutation(string):
    counter = {}
    for char in string.lower().replace(' ', ''):
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    count = 0
    for val in counter.values():
        count += val % 2
    return count <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_palindromePermutation(self):
        for [test_string, expected] in self.data:
            actual = palindromePermutation(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
