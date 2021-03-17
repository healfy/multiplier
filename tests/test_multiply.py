import pytest
from multiplier import multiply_matrix


def test_multiply_quad_matrix():
    mtx1 = [[1, 2], [1, 3]]

    mtx2 = [[2, 3], [4, 1]]

    assert [[10, 5], [14, 6]] == multiply_matrix(mtx1, mtx2)


def test_multiply_simple_matrix():
    mtx1 = [[1, 2], [1, 3], [2, 4]]

    mtx2 = [[2, 3], [4, 1]]

    assert [[10, 5], [14, 6], [20, 10]] == multiply_matrix(mtx1, mtx2)


def test_multiply_un_suit_matrix1():
    mtx1 = [[1, 2], [1, 3]]

    mtx2 = [[2, 3], [4, 1], [1, 2]]
    with pytest.raises(ValueError):
        multiply_matrix(mtx1, mtx2)


def test_multiply_empty_matrix1():
    with pytest.raises(ValueError):
        multiply_matrix(None, [])


def test_multiply__matrix2():
    assert [[2]] == multiply_matrix([[1]], [[2]])
