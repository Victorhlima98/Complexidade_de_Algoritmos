def pesquisa_binaria(a, num):
    esquerda, direita, tentativa = 0, len(a), 1
    while 1:
        meio = (esquerda + direita) // 2
        aux_num = a[meio]
        if num == aux_num:
            return tentativa
        elif num > aux_num:
            esquerda = meio
        else:
            direita = meio
        tentativa += 1


def main(a, v):
    pesquisa_binaria(a, v)