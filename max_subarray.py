def main(array):
    maximo = float('-inf')
    for i in range(0, len(array)):
        c=0
        for j in range(i+1, len(array)):
           c += array[j]
           maximo = max(c, maximo)
    return maximo



