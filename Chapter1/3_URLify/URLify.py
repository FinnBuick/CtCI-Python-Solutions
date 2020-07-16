import unittest


def urlify1(string, length):
    return string[:length].replace(' ', '%20')


def urlify2(string, length):
    char_arr = list(string)
    new_index = len(string)

    for i in reversed(range(length)):
        if char_arr[i] == " ":
            # Replace space char
            char_arr[new_index - 3: new_index] = list("%20")
            new_index -= 3
        else:
            char_arr[new_index - 1] = char_arr[i]
            new_index -= 1
    return "".join(char_arr)


class Test(unittest.TestCase):
    data = [
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith'),
        ('much ado about nothing      ', 22, 'much%20ado%20about%20nothing')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual1 = urlify1(test_string, length)
            self.assertEqual(actual1, expected)
            actual2 = urlify2(test_string, length)
            self.assertEqual(actual2, expected)


if __name__ == "__main__":
    unittest.main()
