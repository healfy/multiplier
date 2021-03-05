import json
import argparse
from multiprocessing import set_start_method

from multiplier import multiply_matrix

if __name__ == '__main__':
    set_start_method('spawn')
    parser = argparse.ArgumentParser()

    parser.add_argument('--m1', help='set matrix in format [[],[]]', type=str)
    parser.add_argument('--m2', help='set matrix in format [[],[]]', type=str)

    args = parser.parse_args()
    mtx1 = json.loads(args.m1)
    mtx2 = json.loads(args.m2)
    if not mtx2 or not mtx1:
        raise ValueError('Invalid value of matrix')
    if len(mtx1) != len(mtx2[0]):
        raise ValueError('this matrix can not be multiplied')
    print(f'Matrix1: {mtx1}')
    print(f'Matrix2: {mtx2}')
    print(f'Result: {multiply_matrix(mtx1, mtx2)}')
