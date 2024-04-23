lista = [1, 2, 3]


def paros_e(a):
    for i in a:
        if i % 2 == 0:
            return True
    return False


print(paros_e(lista))
