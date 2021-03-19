import multiprocessing as mp
import math
from queue import Empty


class Multiprocessor:

    def __init__(self, mtx1: list, mtx2: list, process_number=1):
        self.processes = []
        self.queue = mp.JoinableQueue()
        self.matrix1 = mtx1
        self.matrix2 = mtx2
        self.running = True
        self.process_number = process_number
        self.res = [
            [0 for row in range(len(self.matrix2[0]))]
            for col in range(len(self.matrix1))
        ]

    def get_chunks(self):
        return [(row, col) for row in range(len(self.matrix1))
                for col in range(len(self.matrix2[0]))]

    def _wrapper(self, chunk):
        for elem in chunk:
            self.queue.put(self.multi(*elem))

    def run(self):
        for ch in self.chunks(self.get_chunks(), self.process_number):
            p = mp.Process(target=self._wrapper, args=(ch,))
            self.processes.append(p)
            p.start()

    def wait(self):
        while self.running:
            try:
                indx, value = self.queue.get(timeout=0.05)
                self.res[indx[0]][indx[1]] = value
                self.queue.task_done()
            except Empty:
                self.running = False
        for p in self.processes:
            p.join()
        return self.res

    @staticmethod
    def chunks(lst, n):
        step = math.ceil(len(lst)/n)
        for i in range(0, len(lst), step):
            end = i + step if i + step < len(lst) else len(lst)
            yield lst[i:end]

    def multi(self, row, col):
        res = sum(
            [self.matrix1[row][z] * self.matrix2[z][col]
             for z in range(len(self.matrix1[0]))]
        )
        return (row, col), res


def one_thread(mtx1, mtx2):
    c = [[0 for row in range(len(mtx2[0]))] for col in range(len(mtx1))]
    for i in range(len(mtx1)):
        for j in range(len(mtx2[0])):
            for k in range(len(mtx2)):
                c[i][j] += mtx1[i][k] * mtx2[k][j]
    return c
