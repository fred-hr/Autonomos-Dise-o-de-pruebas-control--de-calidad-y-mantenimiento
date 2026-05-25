from busqueda_binaria import busqueda_binaria


def test_elemento_encontrado():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 7) == 3


def test_elemento_no_encontrado():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 4) == -1


def test_primer_elemento():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 1) == 0


def test_ultimo_elemento():
    lista = [1, 3, 5, 7, 9]
    assert busqueda_binaria(lista, 9) == 4