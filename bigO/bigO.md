# Big O Notation

A **notação Big O** é uma forma de descrever o desempenho de um algoritmo em termos de **tempo de execução** ou **uso de memória**, à medida que o tamanho da entrada cresce. Ela é uma ferramenta fundamental para analisar a eficiência de algoritmos.

---

## 🌟 **Por que usar Big O?**

- **Comparar algoritmos:** Ajuda a entender qual é mais eficiente para diferentes tamanhos de entrada.
- **Previsão de desempenho:** Permite estimar o impacto de grandes quantidades de dados.
- **Foco no pior caso:** Garante que você esteja preparado para os cenários mais exigentes.

---

## ⏱ **Tempo de execução vs. Crescimento**

O tempo de execução de um algoritmo é medido pelo **crescimento** de sua complexidade em relação ao **tamanho da entrada (n)**.

- **Crescimento menor:** Algoritmo mais eficiente.
- **Crescimento maior:** Algoritmo menos eficiente para grandes entradas.

### ⚖ **Comparação de complexidades comuns**
| Notação Big O  | Nome                          | Exemplo de algoritmo            | Crescimento          |
|-----------------|-------------------------------|----------------------------------|----------------------|
| O(1)           | Constante                     | Acesso direto a um índice       | 🔵 Constante         |
| O(log n)       | Logarítmica                   | Busca binária                   | 🔵 Cresce devagar    |
| O(n)           | Linear                        | Iteração simples                | 🟡 Cresce moderado   |
| O(n log n)     | Linear-logarítmica            | Merge Sort, Quick Sort          | 🟡 Moderado/rápido   |
| O(n²)          | Quadrática                    | Bubble Sort, Selection Sort     | 🔴 Cresce rápido     |
| O(2ⁿ)          | Exponencial                   | Problemas de decisão com backtracking | 🔴 Muito rápido  |
| O(n!)          | Fatorial                      | Algoritmos de permutação        | 🔴 Extremamente rápido |

---

## 🛠 **Como analisar a complexidade?**

1. **Identifique o tamanho da entrada (n):** Exemplo: número de elementos em um array.
2. **Conte operações dominantes:** Ignore constantes e termos de menor ordem.
3. **Use a notação Big O:** Expresse o comportamento do algoritmo à medida que o tamanho da entrada cresce indefinidamente (\`n → ∞\`).

---
