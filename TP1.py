import numpy as np
import time

# Criação dos Arrays ----------------------------------------------------------------------------
arrayPrincipal = np.random.randint(-5000, 5000, size=10000)
arrDesordenadoQS = arrayPrincipal.copy()
arrDesordenadoQS_Insertion = arrayPrincipal.copy()
arrDesordenadoQS_MDT = arrayPrincipal.copy()

#------------------------------------------------------------------------------------------------

# Variáveis Globais -----------------------------------------------------------------------------
M = 100  # Valor de M para os sub-vetores gerados

contadorComparacoesQS = 0  # Contar quantos comparações foram feitas
contadorTrocasQS = 0 # Contar quantos trocas foram feitas

contadorComparacaoQS_Insertion = 0
contadorTrocaQS_Insertion = 0

contadorComparacoesQS_MDT = 0
contadorTrocasQS_MDT = 0

#------------------------------------------------------------------------------------------------

#Funções-----------------------------------------------------------------------------------------

# QuickSort Recursivo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Função que executa o quicksort
def quickSort(array, low, high):

    if low < high:

        # Encontrando o pivô
        pi = partition(array, low, high)

        # Chamada recursiva a esquerda do pivo
        quickSort(array, low, pi - 1)

        # Chamada recursiva a direita do pivo
        quickSort(array, pi + 1, high)


# Função para encontrar o pivô e dividir menores que ele á esquerda e maiores à direita
def partition(array, low, high):
    global contadorComparacoesQS
    global contadorTrocasQS 
   
    # Escolha o elemento mais a direita como o pivô
    pivot = array[high]

    #Ponteiro para o maior elemento
    i = low - 1

    # Passe por todos os elementos e compare cada um com o pivô
    for j in range(low, high):
        #contador de comparações
        contadorComparacoesQS += 1

        if array[j] <= pivot:

            # Se elemento menor que pivo, fa;a a troca com o maior elemento apontado por i
            i = i + 1

            # Troca dos elementos
            (array[i], array[j]) = (array[j], array[i])

            #contador de trocas
            contadorTrocasQS += 1

    # Troca o pivo com o maior elemento especificado por i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    #contador de trocas
    contadorTrocasQS += 1

    # Retorna a posiçãode onde a partição está completa
    return i + 1


# Métricas------------------------------------------------------------------------
startQS = time.perf_counter()
quickSort(arrDesordenadoQS, 0, len(arrayPrincipal) - 1)
endQS = time.perf_counter()

totalTimeQS = endQS - startQS

print("\n- - - -  QuickSort Recursivo - - - - -")

print("\nArray desordenado\n", arrayPrincipal)

print("\nArray ordenado:", arrDesordenadoQS)

print('\nQuantidade de Comparações QuickSort: ')
print(contadorComparacoesQS)

print('\nQuantidade de Trocas Quicksort: ')
print(contadorTrocasQS)

print('\nTempo de Execução: ')
print(f"{totalTimeQS} segundos")

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# QuickSort com Inserção = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Mesma função partition do Recursivo
def partition_Insertion(array, low, high):
    global contadorComparacaoQS_Insertion
    global contadorTrocaQS_Insertion

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        contadorComparacaoQS_Insertion +=1
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
            contadorTrocaQS_Insertion += 1

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    contadorTrocaQS_Insertion += 1

    return i + 1

# Função insertion sort
def insertion_sort_qs(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Função do QuickSort com InsertionSort
def quickSort_Insertion(array, low, high, M):
    if low < high:
      if (high - low + 1) > M:
          pi = partition_Insertion(array, low, high)

          quickSort_Insertion(array, low, pi - 1, M)

          quickSort_Insertion(array, pi + 1, high, M)
      else:
        insertion_sort_qs(array, low, high)


# Métricas------------------------------------------------------------------------

startQS_Insertion = time.perf_counter()
quickSort_Insertion(arrDesordenadoQS_Insertion, 0, len(arrayPrincipal) - 1, M)
endQS_Insertion = time.perf_counter()

totalTimeQS_Insertion = endQS_Insertion - startQS_Insertion

print("\n- - - -  QuickSort com Insertion Sort - - - - -")

print("\nArray desordenado\n", arrayPrincipal)

print("\nArray ordenado:", arrDesordenadoQS_Insertion)

print("\nValor de M: ")
print(M)

print('\nQuantidade de Comparações QuickSort com Insertion: ')
print(contadorComparacaoQS_Insertion)

print('\nQuantidade de Trocas Quicksort com Insertion: ')
print(contadorTrocaQS_Insertion)

print('\nTempo de Execução: ')
print(f"{totalTimeQS_Insertion} segundos")


#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# QuickSort com Inserção e Mediana de Três Elementos = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high]

    # Encontra a mediana entre os três elementos
    if (a <= b <= c) or (c <= b <= a):
        median = mid
    elif (b <= a <= c) or (c <= a <= b):
        median = low
    else:
        median = high

    # Coloca o valor da mediana no final para ser utilizado como pivô
    arr[median], arr[high] = arr[high], arr[median]
    return arr[high]

def partition_MDT(arr, low, high):
    global contadorComparacoesQS_MDT
    global contadorTrocasQS_MDT

    pivot = median_of_three(arr, low, high)

    i = low - 1

    for j in range(low, high):
        
        contadorComparacoesQS_MDT += 1

        if arr[j] <= pivot:
            
            i += 1

            contadorTrocasQS_MDT += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    contadorTrocasQS_MDT += 1        
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quicksort_MDT(arr, low, high, M):
    if low < high:
        # Se o tamanho do sub-vetor for menor que M, use insertion sort.
        if high - low + 1 <= M:
            insertion_sort(arr, low, high)
        else:
            pivot_index = partition_MDT(arr, low, high)
            quicksort_MDT(arr, low, pivot_index - 1, M)
            quicksort_MDT(arr, pivot_index + 1, high, M)


# Métricas------------------------------------------------------------------------
startQS_MDT = time.perf_counter()
quicksort_MDT(arrDesordenadoQS_MDT, 0, len(arrayPrincipal) - 1, M)
endQS_MDT = time.perf_counter()

totalTimeQS_MDT = endQS_MDT - startQS_MDT

print("\n- - - -  QuickSort com Insertion Sort e Mediana de tres - - - - -")
print("\nArray desordenado\n", arrayPrincipal)

print("\nArray ordenado:", arrDesordenadoQS_MDT)

print('\nQuantidade de Comparações QuickSort: ')
print(contadorComparacoesQS_MDT)

print('\nQuantidade de Trocas Quicksort com Insertion e Mediana: ')
print(contadorTrocasQS_MDT)

print('\nTempo de Execução: ')
print(f"{totalTimeQS_MDT} segundos")


#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =