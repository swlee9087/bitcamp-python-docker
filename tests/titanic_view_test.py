import unittest

from python.titanic.views.titanic_view import TitanicView


class TitanicViewTest(unittest.TestCase):
    mock = TitanicView()
    def test_modeling(self):

        this = self.mock.preprocessing()


if __name__ == '__main__':
    unittest.main()

