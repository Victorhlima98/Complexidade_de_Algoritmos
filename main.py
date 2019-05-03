import pesquisa_linear
import pesquisa_binaria
import insertion_sort
import merge_sort
import max_subarray
import max_subarray_dc
import utils

if __name__ == '__main__':
    x = 16750
    a = list(range(0, x))
    v = 8
    utils.report_time(pesquisa_linear, (a, v), n_iter=1)
    utils.report_time(pesquisa_binaria, (a, v), n_iter=1)

    a = utils.get_random_list(x)
    utils.report_time(insertion_sort, (a, ), n_iter=1)
    utils.report_time(merge_sort, (a, ), n_iter=1)

    a = utils.get_random_list(x, -x, x)
    utils.report_time(max_subarray, (a, ), n_iter=1)
    utils.report_time(max_subarray_dc, (a, ), n_iter=1)
