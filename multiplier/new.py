import multiprocessing as mp
import math
from queue import Empty


class Multiprocessor:

    def __init__(self, mtx1: list, mtx2: list, process_number=1):
        self.processes = []
        self.queue = mp.Manager().Queue()
        self.matrix1 = mtx1
        self.matrix2 = mtx2
        self.running = True
        self.process_number = process_number

    @staticmethod
    def _wrapper(func, queue: mp.Queue, chunk, mtx1, mtx2):
        for elem in chunk:
            queue.put(func(mtx1, mtx2, *elem))

    def run(self, array: list):
        for ch in self.chunks(array, self.process_number):
            args2 = (self.multi, self.queue, ch, self.matrix1, self.matrix2)
            p = mp.Process(target=self._wrapper, args=args2)
            self.processes.append(p)
            p.start()

    def wait(self):
        rets = [
            [0 for row in range(len(self.matrix2[0]))]
            for col in range(len(self.matrix1))
        ]
        while self.running:
            try:
                indx, value = self.queue.get()
                rets[indx[0]][indx[1]] = value
            except Empty:
                self.running = False
        for p in self.processes:
            p.join()
        return rets

    @staticmethod
    def chunks(lst, n):
        step = math.ceil(len(lst)/n)
        for i in range(0, len(lst), step):
            end = i + step if i + step < len(lst) else len(lst)
            yield lst[i:end]

    @staticmethod
    def multi(mtx1, mtx2, a, b, c):
        return (a, b), mtx1[a][c] * mtx2[c][b]


def one_thread(mtx1, mtx2):
    c = [[0 for row in range(len(mtx2[0]))] for col in range(len(mtx1))]
    for i in range(len(mtx1)):
        for j in range(len(mtx2[0])):
            for k in range(len(mtx2)):
                c[i][j] += mtx1[i][k] * mtx2[k][j]
    return c

