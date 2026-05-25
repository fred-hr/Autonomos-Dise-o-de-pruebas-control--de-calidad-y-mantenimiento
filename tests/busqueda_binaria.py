def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    Retorna el índice del elemento si lo encuentra.
    Retorna -1 si el elemento no existe.
    """

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio

        elif lista[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1