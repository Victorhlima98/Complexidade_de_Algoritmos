from max_crossing_subarray import max_crossing_subarray

from math import floor

def max_sum_subarray(a, low, high):
    if low == high:
        return [low, high, a[low]]
    else:
        center = int(floor((low+high)/2))

        (left_low, left_high, left_sum) = max_sum_subarray(a, low, center)
        (right_low, right_high, right_sum) = max_sum_subarray(a, center+1, high)
        (cross_low, cross_high, cross_sum) = max_crossing_subarray(a, low, center, high)

        if (left_sum >= right_sum) and (left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum) and (right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def main(a):

    return max_sum_subarray(a, 0, len(a) - 1)