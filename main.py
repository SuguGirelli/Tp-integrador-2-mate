# main.py

import funciones

def main():
    # Inicializamos listas para almacenar datos
    dnies = []
    anios_nacimiento = []

    while True:
        dni = input("Ingrese un DNI (solo números) o (fin) para terminar: ")
        if dni.lower() == "fin":
            break
        if dni.isdigit() and len(dni) >= 7:
            dnies.append(dni)
        else:
            print("DNI inválido. Debe contener solo números y tener al menos 7 dígitos.")

    print("\n Entrada de años de nacimiento")
    cantidad_personas = len(dnies)
    for i in range(cantidad_personas):
        while True:
            anio = input(f"Ingrese el año de nacimiento de la persona {i+1}: ")
            if anio.isdigit() and 1900 <= int(anio) <= 2025:
                anios_nacimiento.append(int(anio))
                break
            else:
                print("Año inválido. Debe estar entre 1900 y 2025.")

    # Procesamos DNIs usando funciones externas
    datos_dni = funciones.procesar_dnies(dnies)
    conjuntos_dnis = datos_dni["conjuntos"]
    digitos_totales = datos_dni["digitos_totales"]

    # Mostramos resultados de operaciones con conjuntos
    print("\n Operaciones con conjuntos de digitos")
    print("Unión:", datos_dni["union"])
    print("Intersección:", datos_dni["interseccion"])
    print("Diferencia individual:")
    for i, dif in enumerate(datos_dni["diferencias"]):
        if dif:
            print(f"  DNI {i+1}:", sorted(dif))
        else:
            print(f"  DNI {i+1}: No tiene dígitos exclusivos")
    print("Diferencia simétrica:", datos_dni["diferencia_simetrica"])

    # Verificar condiciones lógicas
    print("\n Evaluacion Logica:")
    if any(len(conjunto) > 6 for conjunto in conjuntos_dnis):
        print("Diversidad numérica alta")
    digitos_compartidos = set.intersection(*conjuntos_dnis)
    for digito in digitos_compartidos:
        print(f"Dígito compartido: {digito}")

    # Conteo de frecuencia de cada dígito
    print("\n Frecuencia de cada digito en c/DNI")
    for i, digitos in enumerate(digitos_totales):
        freq = funciones.calcular_frecuencias(digitos)
        print(f"DNI {i+1} - Frecuencia de dígitos: {freq}")

    # Sumamos el total de dígitos por DNI
    print("\n Suma total de los digitos de los DNIs")
    for i, digitos in enumerate(digitos_totales):
        print(f"DNI {i+1}: {sum(digitos)}")

    # Procesamos los años de nacimiento
    pares = sum(1 for a in anios_nacimiento if a % 2 == 0)
    impares = len(anios_nacimiento) - pares
    print("\n Estadisticas de nacimiento")
    print("Cantidad de personas nacidas en años pares:", pares)
    print("Cantidad de personas nacidas en años impares:", impares)

    if all(a > 2000 for a in anios_nacimiento):
        print("Grupo Z")
    if any(funciones.es_bisiesto(a) for a in anios_nacimiento):
        print("Tenemos un año especial")

    # Cálculo de edades actualesa la fecha
    anio_actual = 2025 
    edades = [anio_actual - a for a in anios_nacimiento]

    # Producto cartesiano entre años y edades
    producto_cartesiano = funciones.calcular_producto_cartesiano(anios_nacimiento, edades)
    print("\n Producto Cartesiano ( año x edades )")
    for par in producto_cartesiano:
        print(par)

# Ejecutar el programa
if __name__ == "__main__":
    main()