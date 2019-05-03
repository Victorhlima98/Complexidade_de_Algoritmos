import random

import time


def report_time(func, inp, n_iter=1000):
    start = time.time()

    for i in range(n_iter):
        func.main(*inp)

    end = time.time()
    total_time = end - start
    print('Total time for %s after %d iterations: %f' % (func.__name__, n_iter, total_time))


def get_random_list(N, min_val=0, max_val=1000):
    listt = [random.randint(min_val, max_val) for _ in range(N)]
    return listt


def get_random_int(min_val=0, max_val=1000):
    return random.randint(min_val, max_val)


def get_random_float(min_val=0, max_val=100):
    return random.uniform(min_val, max_val)
