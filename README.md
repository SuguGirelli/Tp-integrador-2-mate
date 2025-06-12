Parte 1 – Desarrollo Matemático (Conjuntos y Lógica)

1.      Cada integrante debe anotar su número de DNI.

Girelli Nicolás: 41200136
Gomez Julian: 38844753

2.      A partir de los DNIs, se deben formar tantos conjuntos de dígitos únicos como integrantes tenga el grupo.

dni1(41200136) → A = [4, 1, 2, 0, 3, 6]
dni2(38844753) → B = [3, 8, 4, 7, 5]

3.      Realizar entre esos conjuntos las siguientes operaciones: unión, intersección, diferencia (entre pares) y diferencia simétrica.

Unión: A u B = [0, 1, 2, 3, 4, 5, 6, 7, 8]

Intersección: A n B = [3, 4]

Diferencia: A - B = [0, 1, 2, 6]
            B - A = [5, 7, 8]

Diferencia simétrica: A ^ B = [0, 1, 2, 5, 6, 7, 8]

4.      Para cada una de estas operaciones, se debe realizar un diagrama de Venn (a mano o digital), que debe incluirse en la entrega.



5.      Redactar al menos dos expresiones lógicas en lenguaje natural, que puedan luego implementarse en Python y escribir en la documentación que van a presentar cual seria el resultado con los conjuntos que tienen.

* Un año es bisiesto si es divisible por 4 y no es divisible por 100, a menos que también sea divisible por 400 = Función es_bisiesto(anio)

* El DNI es válido si contiene solo números y tiene al menos 7 dígitos = if dni.isdigit() and len(dni) >= 7:
