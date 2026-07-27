# Función para ingresar los valores de una matriz
def completarMatrices(matriz):

    # Recorre todas las filas y columnas de la matriz
    for i in range(2):
        for j in range(3):
            matriz[i][j] = int(input(f"Ingrese el valor de matriz[{i}][{j}]: "))


# Función para mostrar una matriz resultado
def mostrarResultado(R):

    print("\nResultado:")

    # Imprime cada elemento de la matriz
    for i in range(2):
        for j in range(3):
            print(f"{R[i][j]:4}", end="")
        print()


# Función que realiza la suma de dos matrices
def sumaMatriz(A, B):

    R = [[0 for j in range(3)] for i in range(2)]

    # Suma cada elemento de las matrices
    for i in range(2):
        for j in range(3):
            R[i][j] = A[i][j] + B[i][j]

    # Muestra el resultado de la suma
    mostrarResultado(R)


# Función que realiza la resta de dos matrices
def restaMatriz(A, B):

    R = [[0 for j in range(3)] for i in range(2)]

    # Resta cada elemento de las matrices
    for i in range(2):
        for j in range(3):
            R[i][j] = A[i][j] - B[i][j]

    # Muestra el resultado de la resta
    mostrarResultado(R)


# Función que realiza la multiplicación de las matrices
def multiplicacionMatriz(A, B):

    R = [[0 for j in range(3)] for i in range(2)]

    # Multiplica cada elemento de las matrices
    for i in range(2):
        for j in range(3):
            R[i][j] = A[i][j] * B[i][j]

    # Muestra el resultado de la multiplicación
    mostrarResultado(R)


# Función principal
def main():

    # Declaración de las matrices A y B de tamaño 2x3
    A = [[0 for j in range(3)] for i in range(2)]
    B = [[0 for j in range(3)] for i in range(2)]

    # Ingreso de los datos de la matriz A
    print("\nMATRIZ A")
    completarMatrices(A)

    # Ingreso de los datos de la matriz B
    print("\nMATRIZ B")
    completarMatrices(B)

    # Mostrar la suma de las matrices
    print("\nSUMA")
    sumaMatriz(A, B)

    # Mostrar la resta de las matrices
    print("\nRESTA")
    restaMatriz(A, B)

    # Mostrar la multiplicación de las matrices
    print("\nMULTIPLICACION")
    multiplicacionMatriz(A, B)


# Ejecutar el programa
main()