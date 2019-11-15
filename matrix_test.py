from matrix import Matrix
import unittest

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.given = " 9 8 7\n 5 3 2\n 6 6 7"
        self.matrix = Matrix(self.given)

    def test_init(self):
        assert self.matrix.matrix == ['9', '8', '7', '\n', '5', '3', '2', '\n', '6', '6', '7']

    def test_row(self):
        assert self.matrix.rows() == "9, 8, 7\n5, 3, 2\n6, 6, 7"

    def test_column(self):
        assert self.matrix.columns() == "9, 5, 6\n8, 3, 6\n7, 2, 7"
