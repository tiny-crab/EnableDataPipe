import unittest
import numpy as np
from cell_interaction.cell_interaction import cell_type_interactions


class ValidCases(unittest.TestCase):
    def test_small_set(self):
        n_cell_types = 3
        cell_classifications = [0, 1, 2]
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [1, 2]},
            {"cell_id": 1, "neighbors": [0, 2]},
            {"cell_id": 2, "neighbors": [0, 1]},
        ]
        expected = np.array([
            [0, 2, 2],
            [2, 0, 2],
            [2, 2, 0],
        ])

        actual = cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)

        diff = np.testing.assert_array_equal(actual, expected)
        self.assertIsNone(diff)

    def test_medium_set(self):
        n_cell_types = 4
        cell_classifications = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
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

        expected = np.array([
            [12, 6, 6, 6],
            [6, 0, 0, 0],
            [6, 0, 0, 0],
            [6, 0, 0, 0],
        ])

        actual = cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)

        diff = np.testing.assert_array_equal(actual, expected)
        self.assertIsNone(diff)


class NotValidCases(unittest.TestCase):
    def test_empty_classifications(self):
        n_cell_types = 2
        cell_classifications = []
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [3, 1]},
            {"cell_id": 1, "neighbors": [4, 0]},
            {"cell_id": 2, "neighbors": [5]},
            {"cell_id": 3, "neighbors": [0, 4]},
            {"cell_id": 4, "neighbors": [1, 3]},
            {"cell_id": 5, "neighbors": [2]},
        ]
        with self.assertRaises(ValueError):
            cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)

    def test_empty_neighbor_list(self):
        n_cell_types = 2
        cell_classifications = [0, 0, 0, 1, 1, 1]
        cell_neighbors = []

        expected = np.zeros(shape=(n_cell_types, n_cell_types))
        actual = cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)

        diff = np.testing.assert_array_equal(actual, expected)
        self.assertIsNone(diff)

    def test_too_small_cell_types(self):
        n_cell_types = 1
        cell_classifications = [0, 1, 2]
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [1, 2]},
            {"cell_id": 1, "neighbors": [0, 2]},
            {"cell_id": 2, "neighbors": [0, 1]},
        ]

        with self.assertRaises(ValueError):
            cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)


if __name__ == '__main__':
    unittest.main()
