import unittest
import numpy as np
from cell_interaction.cell_interaction import pairwise_logodds_ratio


class MyTestCase(unittest.TestCase):
    def test_small_set(self):
        n_cell_types = 2
        cell_classifications = [0, 0, 0, 1, 1, 1]
        # assuming neighbor dictionary is always symmetrical
        cell_neighbors = [
            {"cell_id": 0, "neighbors": [3, 1]},
            {"cell_id": 1, "neighbors": [4, 0]},
            {"cell_id": 2, "neighbors": [5]},
            {"cell_id": 3, "neighbors": [0, 4]},
            {"cell_id": 4, "neighbors": [1, 3]},
            {"cell_id": 5, "neighbors": [2]},
        ]

        # expected cell type interactions
        #     0     1
        # 0 [ 2 ] [ 6 ]
        # 1 [ 6 ] [ 2 ]

        # expected cell type edges
        #     0     1
        # 0 [ 1 ] [ 3 ]
        # 1 [ 3 ] [ 1 ]

        # expected total edges = 5

        # expected actual frequency
        #      0       1
        # 0 [ 0.2 ] [ 0.6 ]
        # 1 [ 0.6 ] [ 0.2 ]

        # expected proportion by type
        #      0       1
        # 0 [ 0.5 ] [ 0.5 ]

        # expected theo cooccurrence
        #      0        1
        # 0 [ 0.25 ] [ 0.25 ]
        # 1 [ 0.25 ] [ 0.25 ]

        # expected logodds
        #       0         1
        # 0 [  NaN  ] [ 0.301 ]
        # 1 [ 0.301 ] [  NaN  ]

        expected = np.array([
            [0, 6],
            [6, 0],
        ])
        actual = pairwise_logodds_ratio(n_cell_types, cell_classifications, cell_neighbors)

        diff = np.testing.assert_array_equal(actual, expected)
        self.assertIsNone(diff)


if __name__ == '__main__':
    unittest.main()
