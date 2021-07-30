import unittest

from python.modu.template.basic_plot import BasicPlot


class BasicPlotTest(unittest.TestCase):
    mock = BasicPlot()

    def test_plot_show(self):
        self.mock.plot_show()

    def test_plot_two_list_show(self):
        self.mock.plot_two_list_show()

    def test_plot_two_list_show2(self):
        self.mock.plot_two_list_show2()

    def test_plot_two_list_show3(self):
        self.mock.plot_two_list_show3()

    def test_plot_two_list_show4(self):
        self.mock.plot_two_list_show4()

    def test_plot_marker_show(self):
        self.mock.plot_marker_show()

if __name__ == '__main__':
    unittest.main()