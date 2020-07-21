import unittest
from collections import Counter


def oneAway(a, b):
    difference_dict = {}
    count = 0

    for char in a:
        if char in difference_dict:
            difference_dict[char] += 1
        else:
            difference_dict[char] = 1

    for char in b:
        if char in difference_dict:
            difference_dict[char] -= 1
            if difference_dict[char] == 0:
                del difference_dict[char]
        else:
            count += 1

    if count > 1:
        return False
    if len(difference_dict) > 1:
        return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def testOneAway(self):
        for a, b, result in self.data:
            actual = oneAway(a, b)
            self.assertEqual(actual, result)


if __name__ == "__main__":
    unittest.main()
