import unittest
import numpy as np
from cell_interaction.cell_interaction import cell_type_matrix

class MyTestCase(unittest.TestCase):
    def test_small_set(self):
        n_cell_types = 2
        cell_classifications = [0, 0, 0, 1, 1, 1]
        # assuming neighbor dictionary is always complete / bidirectional
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [3]},
            {"cell_id": 1, "neighbors": [4]},
            {"cell_id": 2, "neighbors": [5]},
            {"cell_id": 3, "neighbors": [0]},
            {"cell_id": 4, "neighbors": [1]},
            {"cell_id": 5, "neighbors": [2]},
        ]

        # expected array
        #     0     1
        # 0 [ 0 ] [ 6 ]
        # 1 [ 6 ] [ 0 ]
        expected = np.array([[0, 6], [6, 0]])
        actual = cell_type_matrix(n_cell_types, cell_classifications, cell_neighbors)

        # assert_array_equal returns None when args are equal
        diff = np.testing.assert_array_equal(actual, expected)

        self.assertIsNone(diff)

    def test_medium_set(self):
        n_cell_types = 4
        cell_classifications = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
        # assuming neighbor dictionary is always complete / bidirectional
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [1, 4, 7, 10, 2]},
            {"cell_id": 1, "neighbors": [2, 5, 8, 11, 0]},
            {"cell_id": 2, "neighbors": [0, 3, 6, 9, 1]},
            {"cell_id": 3, "neighbors": [2]},
            {"cell_id": 4, "neighbors": [0]},
            {"cell_id": 5, "neighbors": [1]},
            {"cell_id": 6, "neighbors": [2]},
            {"cell_id": 7, "neighbors": [0]},
            {"cell_id": 8, "neighbors": [1]},
            {"cell_id": 9, "neighbors": [2]},
            {"cell_id": 10, "neighbors": [0]},
            {"cell_id": 11, "neighbors": [1]},
        ]

        # expected array
        #     0     1     2     3
        # 0 [ 12 ] [ 6 ] [ 6 ] [ 6 ]
        # 1 [ 6 ] [ 0 ] [ 0 ] [ 0 ]
        # 2 [ 6 ] [ 0 ] [ 0 ] [ 0 ]
        # 3 [ 6 ] [ 0 ] [ 0 ] [ 0 ]
        expected = np.array([[12, 6, 6, 6], [6, 0, 0, 0], [6, 0, 0, 0], [6, 0, 0, 0]])

        actual = cell_type_matrix(n_cell_types, cell_classifications, cell_neighbors)

        # assert_array_equal returns None when args are equal
        diff = np.testing.assert_array_equal(actual, expected)

        self.assertIsNone(diff)


if __name__ == '__main__':
    unittest.main()
