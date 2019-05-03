def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(n1):
        L.append(a[p + i])

    for j in range(n2):
        R.append(a[q + j + 1])

    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
    return a


def merge_sort(a, p, r):
    if p < r:
        q = ((p + r)/2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        return merge(a, p, q, r)


def main(a):
    return merge_sort(a, 0, len(a)-1)
