from multiprocessing import Manager, cpu_count, Pool


def multi(res: list, mt1, mt2, row: int, col: int):
    res[row][col] = sum([mt1[row][z] * mt2[z][col] for z in range(len(mt1[0]))])


def multiply_matrix(mtx1, mtx2):

    if not mtx2 or not mtx1:
        raise ValueError('Invalid value of matrix')

    if len(mtx1[0]) != len(mtx2):
        raise ValueError('this matrix can not be multiplied')

    proc_list = []
    c = [Manager().list([0 for row in range(len(mtx2[0]))]) for col in
         range(len(mtx1))]
    result = Manager().list(c)

    for row in range(len(mtx1)):
        for col in range(len(mtx2[0])):
            proc_list.append((result, mtx1, mtx2, row, col))

    with Pool(cpu_count()) as pool:
        pool.starmap(multi, proc_list)

    return [list(elem) for elem in result]
