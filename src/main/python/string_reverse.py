def str_rev (str1):
    return str1[::-1]


def str_rev2(str1):
    return ''.join(reversed(str1))


def main():
    str1 = "Hello"
    str2 = "olleH"
    result = str_rev(str1)
    if result == str2:
        print("Success 1")
    result = str_rev2(str1)
    if result == str2:
        print("Success 2")

import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.input_str = "Hello"
        self.result_str = "olleH"

    def test_str_rev(self):
        self.assertEqual(self.result_str, str_rev(self.input_str))

    def test_str_rev2(self):
        self.assertEqual(self.result_str, str_rev(self.input_str))

if __name__ == "__main__":
    unittest.main()
