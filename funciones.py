# funciones.py

from datetime import datetime

def es_bisiesto(anio):
    """Devuelve True si el año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def procesar_dnies(dnies):
    """Procesa los DNIs y devuelve conjuntos, dígitos totales y operaciones con conjuntos."""
    """La función recibe una lista de DNIs y devuelve un diccionario de datosn con clave:valor"""
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

###########################################################
### Funciones python de expresiones en lenguaje natural ### 
###########################################################

# Los dígitos decimales que no están ni en A ni en B
def digitos_no_en_ninguno(A, B):
    todos = set(range(10))
    return todos - (A | B)

# Todos los dígitos pares que estén tanto en A como en B
def digitos_pares_en_ambos(A, B):
    return {x for x in (A & B) if x % 2 == 0}

# Todos los dígitos decimales que conformen el complemento del conjunto A
def complemento_de_A(A):
    todos = set(range(10))
    return todos - A