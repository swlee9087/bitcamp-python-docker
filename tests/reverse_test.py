import unittest

from python.basic.reverse import Reverse


class ReverseTest(unittest.TestCase):
    mock = Reverse()

    def test_str_to_list(self):
        print(input("Input "))
        ls = [i for i in input()]
        self.mock.str_to_list()

    def test_reverse_list(self):
        self.mock.reverse_list()

    def test_list_str(self):
        self.mock.list_to_str()

if __name__ == '__main__':
    unittest.main()
