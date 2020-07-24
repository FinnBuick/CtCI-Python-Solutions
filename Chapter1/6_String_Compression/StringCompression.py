import unittest


def compress(string):
    char_counts = []

    prev = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == prev:
            count += 1
        else:
            char_counts.append(string[i-1] + str(count))
            prev = string[i]
            count = 1

    char_counts.append(string[i-1] + str(count))

    return min(string, ''.join(char_counts), key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [('aabcccccaaa', 'a2b1c5a3'),
            ('abcdef', 'abcdef')]

    def testCompress(self):
        for [test_string, expected] in self.data:
            actual = compress(test_string)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
