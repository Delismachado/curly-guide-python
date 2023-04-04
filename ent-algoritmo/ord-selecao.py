# no modo básico, devo lembrar que a memória do PC é como um conjunto de gavetas
# quando preciso armazenar muitos elementos, posso usar um array ou lista:
    # no array, todos os elemntos ficam um ao lado do outro
    # na lista, os elementos ficam espalhados, mantendo o endereço do próximo elemento
    # arrays permitem leituras rápidas
    # listas permitem rápida inserção e eliminação
    # todos os elemtnos de um arry devem ser do mesmo tipo

def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0

    for i in range(1, len(arr)):
        if (arr[i] < menor):
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoPorSelecao(arr):
    novoArray = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArray.append(arr.pop(menor))
    return novoArray

print(ordenacaoPorSelecao([5,3,7,8,1,9]))