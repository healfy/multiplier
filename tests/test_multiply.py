from multiplier import multiply_matrix


def test_multiply_matrix():
    mtx1 = [[1, 2], [1, 3]]

    mtx2 = [[2, 3], [4, 1]]

    assert [[10, 5], [14, 6]] == multiply_matrix(mtx1, mtx2)
