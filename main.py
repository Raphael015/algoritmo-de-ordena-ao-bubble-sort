def bubble_sort(vetor):
    n = len(vetor)
    troca = True

    while troca:
        troca = False
        for i in range(n - 1):
            if vetor[i] > vetor[i + 1]:
                # Trocar os elementos se estiverem fora de ordem
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True

# Vetor inicial
vetor = [9, 5, 7, 2, 6, 1, 3, 0, 4, 8]

# Chamar a função de ordenação
bubble_sort(vetor)

# Exibir o vetor ordenado
print("Vetor ordenado:", vetor)
