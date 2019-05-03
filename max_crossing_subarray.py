def max_crossing_subarray(a, low, mid, high):
    left_sum= float('-inf')
    sum = 0

    for i in range(mid, low-1,-1):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0

    for j in range(mid + 1, high+1):
        sum += a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

