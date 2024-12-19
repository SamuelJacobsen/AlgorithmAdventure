function somaArray(array) {
    let soma = 0;  // O(1) - Inicialização constante
    for (let elemento of array) {  // O(n) - Percorre todos os elementos do array
        soma += elemento;  // O(1) - Soma cada elemento
    }
    return soma;  // O(1) - Retorna o resultado final
}

// Análise:
// - O loop é o elemento dominante, com O(n).
// - Complexidade total: O(n).
