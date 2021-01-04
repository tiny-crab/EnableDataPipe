import numpy as np


"""
Returns an array containing how many times a cell of type X interacted with a cell of type Y. 
Dimensions: [n_cell_types, n_cell_types]


:param n_cell_types: The number of cell types in this sample
:type n_cell_types: int
:param cell_classifications: A list of cell classifications. The index of the list refers to the cell ID, i.e.
the first element of the list is the cell type of cell ID 0.
:type cell_classifications: list[int]
:param cell_neighbors: A list of dictionaries containing the cell ID and neighbors of each cell in the sample.
:type cell_neighbors: list[object]
"""


def cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors):
    output = np.zeros(shape=(n_cell_types, n_cell_types))

    if not cell_classifications:
        raise ValueError("Cannot compute interaction matrix with empty classification argument")

    if n_cell_types <= max(cell_classifications):
        raise ValueError("Fewer cell types declared than exist in classifications")

    for cell_dict in cell_neighbors:
        cell_id = cell_dict["cell_id"]
        cell_type = cell_classifications[cell_id]
        neighbor_types = [cell_classifications[neighbor] for neighbor in cell_dict["neighbors"]]
        for neighbor_type in neighbor_types:
            output[cell_type, neighbor_type] += 1
            # interactions between cells of the same type will doubled due to input symmetry
            if neighbor_type is not cell_type:
                output[neighbor_type, cell_type] += 1

    return output


"""
Returns matrix containing the log odds ratio between cell type X and cell type Y.
Dimensions: [n_cell_types, n_cell_types]

The log-odds ratio can be defined as the log of the ratio between the actual
frequency of edges between two cell types and their theoretical co-occurrence.

The actual frequency of edges between two cell types is defined as the
proportion of all edges that occur between cells of the two types. For example, 
if the sample had 5 total edges and 2 occurred between cell types A and B,
the actual frequency between cell types A and B = 2⁄5 = 0.4.

The theoretical co-occurrence is the expected frequency of interaction between
two cell types assuming a random placement of cells. For example,
if 50% of edges involve cell type A and 30% involve cell type B,
the theoretical co-occurrence between cell types A and B = 0.5 * 0.3 = 0.15.


:param n_cell_types: The number of cell types in this sample
:type n_cell_types: int
:param cell_classifications: A list of cell classifications. The index of the list refers to the cell ID, i.e.
the first element of the list is the cell type of cell ID 0.
:type cell_classifications: list[int]
:param cell_neighbors: A list of dictionaries containing the cell ID and neighbors of each cell in the sample.
:type cell_neighbors: list[object]
"""


def pairwise_logodds_ratio(n_cell_types, cell_classifications, cell_neighbors):
    if not cell_classifications:
        raise ValueError("Cannot compute interaction matrix with empty classification argument")

    if n_cell_types <= max(cell_classifications):
        raise ValueError("Fewer cell types declared than exist in classifications")

    interaction_matrix = cell_type_interactions(n_cell_types, cell_classifications, cell_neighbors)

    cell_type_edges = interaction_matrix / 2  # reduce number of edges to non-directional connections
    total_edges = 0
    for i in range(n_cell_types):
        edges_of_type = cell_type_edges[i, i:]
        total_edges += np.sum(edges_of_type)

    actual_frequency = cell_type_edges / total_edges

    proportion_by_type = np.sum(cell_type_edges, axis=0) / total_edges

    theo_cooccurrence = np.zeros(shape=(n_cell_types, n_cell_types))
    for i in range(n_cell_types):
        for j in range(n_cell_types):
            theo_cooccurrence[i, j] = proportion_by_type[i] * proportion_by_type[j]

    # TODO what should behavior be in the case of division by 0?
    # This would mean that theo_occurrence is 0.
    # Not sure if this would ever happen to real, and perfect, data, since I assume a cell will always have neighbors.
    # However, if the image data is messy (likely), this could throw errors here. Is this the best behavior, to alert
    # the build to unclean data via an exception? Or should it be fault-tolerant here?
    zero_index = np.where(theo_cooccurrence == 0)
    if zero_index[0].size or zero_index[1].size:
        raise ValueError(f"Theoretical co-occurrence of {zero_index} is 0.")

    return np.log(actual_frequency / theo_cooccurrence)
