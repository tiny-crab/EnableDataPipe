import unittest
import numpy as np
from cell_interaction.cell_interaction import pairwise_logodds_ratio


class MyTestCase(unittest.TestCase):
    def test_small_set(self):
        n_cell_types = 2
        cell_classifications = [0, 0, 0, 1, 1, 1]
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [3, 1]},
            {"cell_id": 1, "neighbors": [4, 0]},
            {"cell_id": 2, "neighbors": [5]},
            {"cell_id": 3, "neighbors": [0, 4]},
            {"cell_id": 4, "neighbors": [1, 3]},
            {"cell_id": 5, "neighbors": [2]},
        ]

        expected_actual_frequency = np.array([
            [0.2, 0.6],
            [0.6, 0.2],
        ])

        expected_theo_cooccurrence = np.array([
            [0.64, 0.64],
            [0.64, 0.64],
        ])

        # TODO I don't like deriving this value by "reprogramming" similar functionality in the unit test
        # However, I prefer it over hardcoding floats that I've taken directly from a sample execution
        expected = np.log(expected_actual_frequency / expected_theo_cooccurrence)
        actual = pairwise_logodds_ratio(n_cell_types, cell_classifications, cell_neighbors)

        diff = np.testing.assert_array_almost_equal(actual, expected, decimal=5)
        self.assertIsNone(diff)


if __name__ == '__main__':
    unittest.main()
