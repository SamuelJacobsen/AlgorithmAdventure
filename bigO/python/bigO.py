def soma_array(array):
    # Inicializa a soma em 0
    soma = 0  # O(1) - Operação constante
    for elemento in array:  # O(n) - Percorre todos os elementos do array
        soma += elemento  # O(1) - Soma cada elemento
    return soma  # O(1) - Retorna o resultado final

# Análise:
# - O loop é o elemento dominante, com O(n).
# - Complexidade total: O(n).