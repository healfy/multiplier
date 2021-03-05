from multiprocessing import Manager, Process


def multi(res: list, mt1, mt2, a: int, b: int, c: int):
    res[a][b] += mt1[a][c] * mt2[c][b]


def multiply_matrix(mtx1, mtx2):
    proc_list = []
    c = [Manager().list([0 for row in range(len(mtx2[0]))]) for col in
         range(len(mtx1))]
    result = Manager().list(c)

    for i in range(len(mtx1)):
        for j in range(len(mtx2[0])):
            for k in range(len(mtx2)):
                p = Process(target=multi, args=(result, mtx1, mtx2, i, j, k))
                proc_list.append(p)

    for pc in proc_list:
        pc.start()

    for pc in proc_list:
        pc.join()

    return [list(elem) for elem in result]
