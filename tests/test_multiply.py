import pytest
from multiplier import multiply_matrix
from multiplier.new import Multiprocessor


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


def test_multi1():
    a = 300
    mt1 = [[1 for i in range(a)] for i in range(a)]
    res = [[a for _ in range(a)] for i in range(a)]
    assert res == multiply_matrix(mt1, mt1)

    # obj = Multiprocessor(mt1, mt1, process_number=4)
    # obj.run()
    # assert res == obj.wait()
