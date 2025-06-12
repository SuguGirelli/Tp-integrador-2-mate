# funciones.py

from datetime import datetime

def es_bisiesto(anio):
    """Devuelve True si el año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def procesar_dnies(dnies):
    """Procesa los DNIs y devuelve conjuntos, dígitos totales y operaciones con conjuntos."""
    conjuntos_dnis = [set(dni) for dni in dnies]
    digitos_totales = [list(map(int, dni)) for dni in dnies]

    # Operaciones con conjuntos
    union = set()
    interseccion = None
    diferencias = []
    diferencia_simetrica = set()

    for conjunto in conjuntos_dnis:
        union |= conjunto
        diferencia_simetrica ^= conjunto
        if interseccion is None:
            interseccion = conjunto.copy()
        else:
            interseccion &= conjunto

    for i in range(len(conjuntos_dnis)):
        otros = set()
        for j in range(len(conjuntos_dnis)):
            if i != j:
                otros |= conjuntos_dnis[j]
        diferencias.append(conjuntos_dnis[i] - otros)

    return {
        'conjuntos': conjuntos_dnis,
        'digitos_totales': digitos_totales,
        'union': sorted(union),
        'interseccion': sorted(interseccion) if interseccion else [],
        'diferencias': diferencias,
        'diferencia_simetrica': sorted(diferencia_simetrica)
    }

def calcular_frecuencias(digitos):
    """Calcula la frecuencia de cada dígito en una lista de dígitos."""
    freq = {}
    for d in digitos:
        freq[d] = freq.get(d, 0) + 1
    return freq

def calcular_producto_cartesiano(anios, edades):
    """Devuelve el producto cartesiano entre años y edades."""
    return [(a, e) for a in anios for e in edades]