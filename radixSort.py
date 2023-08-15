def countingSort(arr, factor):
    count = [0]*10

    # Contagem de dígitos
    for v in arr:
        count[(v//factor)%10] += 1 # Dígito na posição atual

    # Contagem cumulativa
    for i in range(1,10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    output = [0]*len(arr)
    for i in range(len(arr), 0, -1):
        currDig = (arr[i-1] // factor) % 10
        output[count[currDig] - 1] = arr[i-1]
        count[currDig] -= 1


    # Copiando lista ordenada
    for i in range(len(arr)):
        arr[i] = output[i]



def sort(arr):
    m = max(arr)
    exp = 0 # Exponencial: define qual dígito está sendo considerado para a ordenação no momento
    while m // (10**exp) > 0: # Repete enquanto exp está na ordem de grandeza do maior elemento da lista
        countingSort(arr, 10**exp)
        exp += 1 # Aumenta ordem de grandeza, para pegar próximo dígito

arr = [7,128,273,36,2,6,3]
sort(arr)
print(arr)
